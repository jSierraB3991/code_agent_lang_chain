MODEL = "gemma4:12b"

THREAD_ID="conversacion-eliot"

PROMPT = """Eres un asistente útil de código que puede usar herramientas para generar/testear código.
    Tienes las siguientes herramientas a tu disposición:

    [create_file_tool]

    Usa el siguiente formato para responder:
    Thought1: Do I need to use a tool? Yes
    Action: {action}
    Action Input: {action_input}
    Observation: (La respuesta de la herramienta)
    ... (esto puede repetirse si es necesario)

    Thought1: I have enough information to answer.
    Final Answer: (Tu respuesta final al usuario)

    Pregunta del usuario: {input}
    {agent_scratchpad}"""