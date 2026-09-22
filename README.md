# Local Code Agent

Agente de código local construido con **Python, LangChain, LangGraph y Ollama**.

El agente utiliza un modelo ejecutado localmente mediante Ollama y dispone de un conjunto de herramientas para interactuar con el sistema de archivos, ejecutar tests de Python y comunicarse con el usuario mediante notificaciones y preguntas interactivas.

## Características

- 🤖 Ejecución de modelos locales mediante Ollama.
- 🛠️ Agente basado en LangChain.
- 🧠 Persistencia del estado de las conversaciones mediante SQLite y LangGraph.
- 📁 Manipulación del sistema de archivos mediante herramientas controladas.
- 🧪 Ejecución de tests de Python.
- 🔔 Notificaciones de escritorio.
- ❓ Preguntas interactivas con opciones o texto libre.
- ⌨️ Interfaz interactiva desde terminal.
- 🛑 Control del ciclo de ejecución mediante `exit`, `quit`, `clear` y `cls`.

## Arquitectura

El proyecto separa el agente de las herramientas que puede utilizar:

```text
src/
├── agent/
│   └── ...
├── libs/
│   ├── colors.py
│   ├── constants.py
│   └── methods.py
├── tools/
│   ├── file_system/
│   │   ├── change_path.py
│   │   ├── create_directory.py
│   │   ├── create_file.py
│   │   ├── delete_directory.py
│   │   ├── delete_file.py
│   │   ├── file_reader_tool.py
│   │   ├── list_files_tool.py
│   │   └── move_file.py
│   ├── notificaciones/
│   │   ├── ask_choice_tool.py
│   │   ├── ask_user_tool.py
│   │   └── plyer_notifications.py
│   └── test_runner/
│       └── run_python.py
└── ...

test/
└── ...

checkpoints.sqlite
```

## Herramientas

### Sistema de archivos

El agente puede utilizar herramientas específicas para:

| Herramienta             | Función                       |
| ----------------------- | ----------------------------- |
| `create_file_tool`      | Crear archivos                |
| `read_file_tool`        | Leer archivos                 |
| `list_files_tool`       | Listar archivos y directorios |
| `create_directory_tool` | Crear directorios             |
| `change_path_tool`      | Cambiar de directorio         |
| `delete_file_tool`      | Eliminar archivos             |
| `delete_directory_tool` | Eliminar directorios          |
| `move_file_tool`        | Mover archivos                |

Las operaciones son expuestas al modelo como **tools**, en lugar de darle acceso directo a una shell.

### Tests

`run_python_tests_tool` permite ejecutar los tests de Python del proyecto.

La ejecución utilizada para verificar el proyecto es:

```bash
python -m pytest ./src test/
```

### Notificaciones

El agente dispone de tres mecanismos de interacción:

- `show_notification_tool` — muestra una notificación de escritorio.
- `ask_choice_tool` — solicita al usuario elegir entre varias opciones.
- `ask_user_tool` — permite solicitar una respuesta escrita al usuario.

Esto permite que una herramienta no solamente devuelva información al modelo, sino que también pueda solicitar una decisión al usuario.

## Modelo

El agente utiliza `ChatOllama`:

```python
llm = ChatOllama(
    model=model,
    temperature=0
)
```

El modelo se proporciona al crear el agente:

```python
agent = Agent(
    model="qwen2.5-coder:3b",
    thread_id="main"
)
```

Puedes utilizar cualquier modelo compatible con Ollama que soporte las capacidades requeridas por el agente.

## Persistencia

LangGraph utiliza `SqliteSaver` para almacenar los checkpoints:

```python
with SqliteSaver.from_conn_string("checkpoints.sqlite") as checkpointer:
```

Cada ejecución utiliza un `thread_id`:

```python
self.config = {
    "configurable": {
        "thread_id": thread_id
    }
}
```

Esto permite mantener el estado asociado a una conversación entre diferentes invocaciones del agente.

## Requisitos

- Python 3
- Ollama
- Un modelo compatible instalado en Ollama
- Dependencias del proyecto

Instala las dependencias con el método utilizado por tu entorno Python.

Por ejemplo, si el proyecto utiliza `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Configuración de Ollama

Comprueba que Ollama esté disponible:

```bash
ollama list
```

Si el modelo todavía no está instalado:

```bash
ollama pull qwen2.5-coder:3b
```

También puedes utilizar otro modelo compatible.

## Ejecución

Inicia el agente desde el punto de entrada del proyecto:

```bash
python -m src
```

> El comando exacto depende del módulo utilizado como punto de entrada.

Una vez iniciado:

```text
Escribe 'exit' para salir
```

Puedes introducir instrucciones normalmente:

```text
> lee test.txt y dime qué contiene
```

El agente decidirá qué herramientas necesita utilizar para realizar la tarea.

## Comandos de la terminal

Durante la ejecución existen algunos comandos especiales:

| Comando | Acción              |
| ------- | ------------------- |
| `exit`  | Salir del agente    |
| `quit`  | Salir del agente    |
| `clear` | Limpiar la pantalla |
| `cls`   | Limpiar la pantalla |

También puedes utilizar `Ctrl+C` para interrumpir una operación.

## Flujo de ejecución

De forma simplificada:

```text
Usuario
   │
   ▼
Terminal
   │
   ▼
Agent
   │
   ├──► Ollama / LLM
   │
   ├──► File System Tools
   │
   ├──► Test Runner
   │
   └──► Notification Tools
             │
             ▼
           Usuario

   │
   ▼
LangGraph Checkpointer
   │
   ▼
SQLite
```

El modelo no ejecuta directamente comandos del sistema. Las acciones disponibles se encuentran definidas explícitamente en la lista `tools`:

```python
tools = [
    create_file_tool,
    read_file_tool,
    list_files_tool,
    create_directory_tool,
    change_path_tool,
    delete_file_tool,
    delete_directory_tool,
    move_file_tool,

    run_python_tests_tool,

    ask_choice_tool,
    ask_user_tool,
    show_notification_tool,
]
```

Esto permite ampliar las capacidades del agente agregando nuevas herramientas sin modificar directamente el funcionamiento del modelo.

## Objetivo

El proyecto busca construir un **agente de código local y extensible**, donde el modelo se encarga de razonar sobre las tareas y las operaciones reales se realizan mediante herramientas explícitamente definidas.

La arquitectura permite agregar progresivamente nuevas capacidades como herramientas para Git, búsqueda de código, análisis de proyectos, ejecución de comandos controlados o integración con otros servicios.
