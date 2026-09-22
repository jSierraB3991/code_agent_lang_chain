from plyer import notification
from langchain.tools import tool

@tool(name_or_callable="show_notification_tool", description="Muestra notificaciones al usuario, importe, app_icon para darle el tipo de notificación")
def show_notification_tool(message: str, app_icon: str) -> str:
    """
    Muestra una notificación utilizando plyer.
    
    Args:
        message (str): Mensaje de la notificación
        app_icon (str): info/error 
    """
    try:
        app_name = "Code Agent LangChain"
        title = "Notificación del agente de código"
        notification.notify(
            title=title,
            message=message,
            timeout=5,
            app_name=app_name,
            app_icon=app_icon,
        )
        return f"Notificación mostrada: {title} - {message}"
    except Exception as e:
        return f"Error al mostrar notificación: {e}"
