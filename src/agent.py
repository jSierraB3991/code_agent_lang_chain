from libs.colors import RED, YELLOW, RESET
from libs.constants import PROMPT
from libs.methods import clear_screen, stop_model

from tools.tools import tools

from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.types import Checkpointer

class Agent:

    def __init__(self, model: str, thread_id: str):
        llm = ChatOllama(model=model, temperature=0)
        self.model = model
        self.llm = llm.model_copy()
        self.config = {"configurable": {"thread_id": thread_id}}


    def run_agent(self, user_input: str, check_pointer: Checkpointer):
        executor = create_agent(
            model=self.llm, 
            tools=tools, 
            system_prompt=PROMPT,
            checkpointer=check_pointer
        )
        result = executor.invoke(
            {"messages": [("user", user_input)]}, 
            config=self.config
        )

        for i, message in enumerate(result["messages"]):
            print(f"\n===== MESSAGE {i} =====")
            print("TYPE:", type(message).__name__)
            print("CONTENT:", repr(message.content))
            print("TOOL_CALLS:", getattr(message, "tool_calls", None))
            print("TOOL_NAME:", getattr(message, "name", None))
        stop_model(self.model)

    def print_bye(self, message="adiós", tipo_color=RED):
        emoji = "👋"
        print(f"{tipo_color}{YELLOW} {emoji} {message} {RESET}")
        pass

    def run_user_input(self, user_name: str = "Eliot"):
        with SqliteSaver.from_conn_string("checkpoints.sqlite") as checkpointer:
            print("Escribe 'exit' para salir")
            while True:
                try:
                    user_input = input(f"{YELLOW}{user_name} {self.model} {RESET} > ")
                except KeyboardInterrupt as e:
                    self.print_bye("Saliendo por interrupción")
                    break

                if user_input.lower() in ("exit", "quit"):
                    self.print_bye(f"adiós {user_name}")
                    break
                if user_input.lower() in ("clear", "cls"):
                    clear_screen()
                    continue
                if not user_input.strip():
                    continue
                try:
                    self.run_agent(user_input.strip(), checkpointer)
                except KeyboardInterrupt:
                    print("Escribe 'exit' para salir")
                    continue

