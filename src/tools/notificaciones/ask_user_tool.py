from langchain.tools import tool

@tool(name_or_callable="ask_user_tool", description="Le permite al usuario escribir una duda que el modelo tenga")
def ask_user_tool(question: str) -> str:
    """
    Le permite al usuario escribir una duda que el modelo tenga
    
    Args:
        question (str): La pregunta puntual que el llm tiene
        
    Returns:
        str: respuesta, sin cambio del usuario
    """
    print(question)
    return input("\nRespuesta: ")