"""
Ejemplos de uso de GitHub Copilot - Función Agent

Esta sesión práctica demuestra cómo usar GitHub Copilot como agente
para resolver tareas complejas y crear código desde cero.

Instrucciones para usar Copilot Agent:
1. Abre el panel de Copilot Chat
2. Describe tareas complejas que quieres que Copilot resuelva
3. Pide a Copilot que genere código completo para funcionalidades específicas
4. Usa los prompts de ejemplo listados abajo

PROMPTS DE AGENTE PARA PRACTICAR:

1. Generación de código completo:
   "Create a complete REST API client class for managing users"
   "Generate a data validation system with custom validators"
   "Build a complete logging system with file rotation"

2. Análisis y solución de problemas:
   "Analyze this codebase and suggest architectural improvements"
   "Create a complete test suite for this module"
   "Design a caching system for this application"

3. Implementación de patrones:
   "Implement the Observer pattern for event handling"
   "Create a decorator-based authentication system"
   "Build a factory pattern for creating different database connections"
"""

# EJERCICIO 1: Pide a Copilot Agent que genere código completo
"""
PROMPT PARA COPILOT AGENT:
"Create a complete configuration management system that can:
1. Load configuration from JSON, YAML, and environment variables
2. Support nested configuration with dot notation access
3. Include validation and default values
4. Support configuration hot reloading
5. Include proper error handling and logging"

Pega el resultado aquí:
"""
# [El código generado por Copilot irá aquí]


# EJERCICIO 2: Sistema de cache
"""
PROMPT PARA COPILOT AGENT:
"Create a comprehensive caching system that includes:
1. In-memory cache with TTL support
2. LRU eviction policy
3. Thread-safe operations
4. Decorators for easy function caching
5. Statistics and monitoring
6. Serialization support for complex objects"

Pega el resultado aquí:
"""
# [El código generado por Copilot irá aquí]


# EJERCICIO 3: Sistema de validación de datos
"""
PROMPT PARA COPILOT AGENT:
"Build a complete data validation framework that provides:
1. Chainable validators (required, min_length, max_length, email, etc.)
2. Custom validator support
3. Nested object validation
4. Detailed error messages with field paths
5. Schema-based validation
6. Integration with dataclasses and Pydantic-style models"

Pega el resultado aquí:
"""
# [El código generado por Copilot irá aquí]


# EJERCICIO 4: Cliente HTTP avanzado
"""
PROMPT PARA COPILOT AGENT:
"Create an advanced HTTP client class that includes:
1. Automatic retry with exponential backoff
2. Request/response middleware support
3. Authentication handlers (Bearer, Basic, API Key)
4. Response caching
5. Request rate limiting
6. Comprehensive logging
7. Timeout configuration
8. JSON/XML response parsing"

Pega el resultado aquí:
"""
# [El código generado por Copilot irá aquí]


# EJERCICIO 5: Sistema de eventos
"""
PROMPT PARA COPILOT AGENT:
"Implement a complete event system that supports:
1. Event registration and emission
2. Synchronous and asynchronous event handlers
3. Event priorities and ordering
4. Event filtering and conditions
5. Wildcard event subscriptions
6. Event history and replay
7. Error handling in event handlers
8. Performance monitoring"

Pega el resultado aquí:
"""
# [El código generado por Copilot irá aquí]


# EJERCICIO 6: Base de datos ORM simple
"""
PROMPT PARA COPILOT AGENT:
"Create a simple ORM system that provides:
1. Model definition with field types
2. Database connection management
3. CRUD operations (Create, Read, Update, Delete)
4. Query builder with method chaining
5. Relationships (one-to-one, one-to-many)
6. Migration support
7. Connection pooling
8. Transaction support"

Pega el resultado aquí:
"""
# [El código generado por Copilot irá aquí]


# EJERCICIO 7: Sistema de archivos con monitoreo
"""
PROMPT PARA COPILOT AGENT:
"Build a file system monitoring and management tool that:
1. Watches directories for file changes
2. Processes files based on patterns and rules
3. Supports file operations (copy, move, delete, archive)
4. Includes file integrity checking (checksums)
5. Provides detailed logging of all operations
6. Supports batch processing
7. Has configurable filters and actions
8. Includes error recovery mechanisms"

Pega el resultado aquí:
"""
# [El código generado por Copilot irá aquí]


# EJERCICIO 8: Analizador de rendimiento
"""
PROMPT PARA COPILOT AGENT:
"Create a performance monitoring and profiling system that:
1. Tracks function execution times
2. Memory usage monitoring
3. Decorator-based profiling
4. Report generation (text, HTML, JSON)
5. Statistical analysis (min, max, avg, percentiles)
6. Call graph generation
7. Bottleneck identification
8. Real-time monitoring dashboard data"

Pega el resultado aquí:
"""
# [El código generado por Copilot irá aquí]


# EJERCICIO 9: Task scheduler/queue system
"""
PROMPT PARA COPILOT AGENT:
"Implement a task scheduling and queue system that supports:
1. Delayed task execution
2. Recurring tasks with cron-like scheduling
3. Task priorities and categories
4. Worker pool management
5. Task persistence and recovery
6. Progress tracking and callbacks
7. Error handling and retry logic
8. Monitoring and statistics"

Pega el resultado aquí:
"""
# [El código generado por Copilot irá aquí]


# EJERCICIO 10: API Testing framework
"""
PROMPT PARA COPILOT AGENT:
"Create a comprehensive API testing framework that includes:
1. Request builder with fluent interface
2. Response assertion library
3. Test case management and organization
4. Mock server capabilities
5. Data generation and fixtures
6. Test reporting (HTML, JSON, JUnit)
7. Performance testing capabilities
8. Environment and configuration management"

Pega el resultado aquí:
"""
# [El código generado por Copilot irá aquí]


# EJEMPLO DE CÓDIGO EXISTENTE PARA MEJORAR CON AGENT
class SimpleCalculator:
    """
    PROMPT PARA COPILOT AGENT:
    "Analyze this simple calculator class and extend it into a 
    comprehensive mathematical expression evaluator that supports:
    1. Complex mathematical expressions with parentheses
    2. Mathematical functions (sin, cos, log, sqrt, etc.)
    3. Variables and constants
    4. Unit conversions
    5. Equation solving
    6. Graphing capabilities
    7. History and memory functions
    8. Error handling for invalid expressions"
    """
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result


class BasicFileProcessor:
    """
    PROMPT PARA COPILOT AGENT:
    "Transform this basic file processor into a comprehensive 
    document processing pipeline that supports:
    1. Multiple file formats (PDF, Word, Excel, CSV, JSON, XML)
    2. Content extraction and parsing
    3. Data transformation and cleaning
    4. Template-based document generation
    5. Batch processing with progress tracking
    6. Plugin system for custom processors
    7. Validation and error reporting
    8. Metadata extraction and indexing"
    """
    
    def __init__(self):
        self.processed_files = []
    
    def read_file(self, filename):
        with open(filename, 'r') as f:
            return f.read()
    
    def write_file(self, filename, content):
        with open(filename, 'w') as f:
            f.write(content)


if __name__ == "__main__":
    print("=== Ejemplos para Copilot Agent ===")
    print("Usa Copilot Agent para generar código completo y sistemas complejos")
    print("Copia los prompts en Copilot Chat y pega los resultados en este archivo")
    
    # Prueba las clases existentes
    calc = SimpleCalculator()
    print(f"Suma: {calc.add(5, 3)}")
    print(f"Historial: {calc.history}")
    
    processor = BasicFileProcessor()
    print("Procesador de archivos básico creado")