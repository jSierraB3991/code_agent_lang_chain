from libs.colors import RED, YELLOW, RESET
from libs.constants import MODEL, PROMPT, THREAD_ID
from libs.methods import clear_screen

from tools.tools import tools

from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.types import Checkpointer

class Agent:

    def __init__(self):
        self.llm = ChatOllama(model=MODEL)
        self.config = {"configurable": {"thread_id": THREAD_ID}}

        with SqliteSaver.from_conn_string("checkpoints.sqlite") as checkpointer:
            self.run_agent(user_input="Quiero que te presentes y me saludes, en caso de no saber esto datos, quiero que me los pidas", check_pointer=checkpointer)

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
        resp_final = result["messages"][-1].content
        print(f"{MODEL} Respuesta: {resp_final}")

    def print_bye(self, message="adiós", tipo_color=RED):
        emoji = "👋"
        print(f"{tipo_color}{YELLOW} {emoji} {message} {RESET}")
        pass

    def run_user_input(self, user_name: str = "Eliot"):
        with SqliteSaver.from_conn_string("checkpoints.sqlite") as checkpointer:
            print("Escribe 'exit' para salir")
            while True:
                try:
                    user_input = input(f"{user_name} {MODEL} > ")
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

