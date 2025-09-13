# Sesión Práctica GitHub Copilot - Python

## Descripción
Esta es una sesión práctica en Python para aprender y utilizar las principales funciones de GitHub Copilot:
- **Inline**: Sugerencias automáticas mientras escribes código
- **Ask**: Hacer preguntas específicas a Copilot
- **Edit**: Usar comandos para editar y mejorar código existente
- **Agent**: Usar Copilot para generar sistemas completos

## Estructura del Proyecto

```
sesion01/
├── README.md                    # Este archivo
├── requirements.txt             # Dependencias de Python
├── examples/                    # Ejemplos demostrativos
│   ├── __init__.py
│   ├── inline_examples.py       # Ejemplos de sugerencias inline
│   ├── ask_examples.py          # Ejemplos para hacer preguntas
│   ├── edit_examples.py         # Ejemplos de edición de código
│   └── agent_examples.py        # Ejemplos de Copilot como agente
├── exercises/                   # Ejercicios prácticos
│   ├── __init__.py
│   ├── exercise_1_inline.py     # Práctica con sugerencias inline
│   ├── exercise_2_ask.py        # Práctica haciendo preguntas
│   ├── exercise_3_edit.py       # Práctica editando código
│   └── exercise_4_agent.py      # Práctica con agente
└── utils/                       # Utilidades y funciones helper
    ├── __init__.py
    └── helpers.py               # Funciones de utilidad
```

## Requisitos Previos

### Software Necesario
- Python 3.8 o superior
- Visual Studio Code
- Extensión de GitHub Copilot para VS Code
- Git

### Configuración
1. Clona este repositorio
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Abre el proyecto en VS Code
4. Asegúrate de que GitHub Copilot esté activado

## Guía de la Sesión

### 1. Copilot Inline (30 minutos)
- **Archivo**: `examples/inline_examples.py`
- **Ejercicio**: `exercises/exercise_1_inline.py`

**Qué aprenderás:**
- Cómo funciona las sugerencias automáticas
- Cuándo aceptar o rechazar sugerencias
- Técnicas para obtener mejores sugerencias
- Completado automático de funciones y clases

**Instrucciones:**
1. Abre `examples/inline_examples.py`
2. Coloca el cursor después de cada comentario "# Escribe aquí"
3. Comienza a escribir y observa las sugerencias
4. Acepta con `Tab`, rechaza con `Esc`
5. Completa el ejercicio en `exercises/exercise_1_inline.py`

### 2. Copilot Ask (30 minutos)
- **Archivo**: `examples/ask_examples.py`
- **Ejercicio**: `exercises/exercise_2_ask.py`

**Qué aprenderás:**
- Cómo hacer preguntas efectivas a Copilot
- Análisis y explicación de código existente
- Identificación de problemas y mejoras
- Debugging asistido por Copilot

**Instrucciones:**
1. Abre el panel de Copilot Chat (`Ctrl+Shift+I` / `Cmd+Shift+I`)
2. Selecciona código y haz preguntas específicas
3. Prueba diferentes tipos de preguntas
4. Completa el ejercicio documentando las respuestas

### 3. Copilot Edit (30 minutos)
- **Archivo**: `examples/edit_examples.py`
- **Ejercicio**: `exercises/exercise_3_edit.py`

**Qué aprenderás:**
- Comandos `/edit` para refactoring automático
- Mejora de código existente
- Optimización y limpieza de código
- Conversión de patrones de código

**Instrucciones:**
1. Selecciona el código a editar
2. Usa comandos `/edit` en Copilot Chat
3. Aplica las sugerencias de mejora
4. Compara antes y después

### 4. Copilot Agent (45 minutos)
- **Archivo**: `examples/agent_examples.py`
- **Ejercicio**: `exercises/exercise_4_agent.py`

**Qué aprenderás:**
- Generación de sistemas completos
- Resolución de problemas complejos
- Arquitectura de software asistida
- Creación de frameworks y librerías

**Instrucciones:**
1. Usa prompts detallados para sistemas completos
2. Refina y mejora el código generado
3. Integra diferentes componentes
4. Prueba y valida los sistemas creados

## Comandos Útiles

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Ejecutar ejemplos
```bash
python examples/inline_examples.py
python examples/ask_examples.py
python examples/edit_examples.py
python examples/agent_examples.py
```

### Ejecutar ejercicios
```bash
python exercises/exercise_1_inline.py
python exercises/exercise_2_ask.py
python exercises/exercise_3_edit.py
python exercises/exercise_4_agent.py
```

### Ejecutar tests (si los implementas)
```bash
python -m pytest tests/ -v
```

## Atajos de Teclado Importantes

| Función | Windows/Linux | macOS |
|---------|---------------|-------|
| Aceptar sugerencia inline | `Tab` | `Tab` |
| Rechazar sugerencia inline | `Esc` | `Esc` |
| Abrir Copilot Chat | `Ctrl+Shift+I` | `Cmd+Shift+I` |
| Siguiente sugerencia | `Alt+]` | `Option+]` |
| Sugerencia anterior | `Alt+[` | `Option+[` |

## Tips para Usar Copilot Efectivamente

### 1. Para Inline
- Usa nombres de variables y funciones descriptivos
- Escribe comentarios claros sobre lo que quieres hacer
- Proporciona contexto con imports y definiciones
- Comienza a escribir para activar sugerencias

### 2. Para Ask
- Haz preguntas específicas y contextuales
- Selecciona el código relevante antes de preguntar
- Usa preguntas como:
  - "¿Qué hace esta función?"
  - "¿Cómo puedo optimizar esto?"
  - "¿Hay algún error en este código?"

### 3. Para Edit
- Selecciona exactamente el código a editar
- Usa comandos específicos como:
  - `/edit refactor this function`
  - `/edit add error handling`
  - `/edit convert to list comprehension`

### 4. Para Agent
- Proporciona requisitos detallados y específicos
- Incluye ejemplos de uso esperado
- Pide código de prueba y documentación
- Refina iterativamente el resultado

## Evaluación y Puntuación

| Ejercicio | Puntos Máximos | Criterios |
|-----------|----------------|-----------|
| Inline | 30 | Completado de funciones, uso efectivo de sugerencias |
| Ask | 50 | Preguntas realizadas, mejoras implementadas |
| Edit | 50 | Comandos usados, refactoring aplicado |
| Agent | 100 | Sistemas implementados, refinamiento, documentación |
| **Total** | **230** | |

## Recursos Adicionales
- [Documentación oficial de GitHub Copilot](https://docs.github.com/en/copilot)
- [Best practices para Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)
- [Copilot en VS Code](https://code.visualstudio.com/docs/editor/github-copilot)

## Soporte
Si tienes problemas durante la sesión:
1. Verifica que Copilot esté activado en VS Code
2. Revisa la configuración de la extensión
3. Consulta con el instructor
4. Revisa los logs de Copilot en VS Code

---

¡Disfruta aprendiendo con GitHub Copilot! 🚀
