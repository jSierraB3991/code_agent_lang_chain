from langchain.tools import tool

@tool(name_or_callable="ask_choice_tool", description="Le permite elegir al usuario una de las opciones que le da el llm")
def ask_choice_tool(question: str, options: list[str]) -> str:
    """
    Le permite al usuario seleccionar una de las opciones que puede dar el llm
    
    Args:
        question (str): La pregunta puntual que el llm tiene
        options (list[str]): opciones que se le pueda dar a esa pregunta
        
    Returns:
        str: opción seleccionada por el usuario
    """
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        answer = input("\nRespuesta: ")

        if answer.isdigit():
            index = int(answer) - 1

            if 0 <= index < len(options):
                return options[index]

        print("Opción inválida.")


