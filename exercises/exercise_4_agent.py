"""
EJERCICIO 4: Práctica con Copilot Agent

Objetivo: Usar Copilot como agente para generar sistemas completos y resolver problemas complejos.

Instrucciones:
1. Copia cada prompt en Copilot Chat
2. Pega el código generado en las secciones indicadas
3. Prueba y refina el código con Copilot
4. Documenta el proceso y resultados

PUNTUACIÓN:
- Prompt usado correctamente: 2 puntos
- Código generado funciona: 3 puntos
- Refinamiento y mejoras: 3 puntos
- Documentación del proceso: 2 puntos
- Total posible: 100 puntos
"""


# DESAFÍO 1: Sistema de Validación de Datos
"""
PROMPT PARA COPILOT AGENT:
"Create a comprehensive data validation system for Python that includes:
1. A base Validator class with chainable validation rules
2. Built-in validators: required, min_length, max_length, email, phone, numeric, date
3. Custom validator support with lambda functions
4. Detailed error messages with field paths for nested objects
5. Schema-based validation for dictionaries
6. Integration with dataclasses for automatic validation
7. Performance optimized with caching
8. Example usage and test cases

Make it production-ready with proper error handling, type hints, and documentation."

RESULTADO DE COPILOT:
[Pega aquí el código generado por Copilot]

PROCESO DE REFINAMIENTO:
[Documenta aquí las mejoras que pediste a Copilot]

CÓDIGO FINAL:
"""
# Pega aquí el código final del sistema de validación


# DESAFÍO 2: Cache System Inteligente
"""
PROMPT PARA COPILOT AGENT:
"Build an intelligent caching system that features:
1. Multiple storage backends (memory, file, Redis-compatible interface)
2. TTL (Time To Live) with automatic expiration
3. LRU (Least Recently Used) eviction policy
4. Thread-safe operations with proper locking
5. Decorator for easy function result caching
6. Cache statistics and monitoring
7. Serialization support for complex objects (JSON, pickle)
8. Cache warming and preloading capabilities
9. Configurable cache policies per key pattern
10. Performance metrics and profiling

Include comprehensive examples and benchmarking code."

RESULTADO DE COPILOT:
[Pega aquí el código generado por Copilot]

PROCESO DE REFINAMIENTO:
[Documenta aquí las mejoras que pediste a Copilot]

CÓDIGO FINAL:
"""
# Pega aquí el código final del sistema de cache


# DESAFÍO 3: API Client Framework
"""
PROMPT PARA COPILOT AGENT:
"Create a robust HTTP API client framework that provides:
1. Fluent interface for building requests (method chaining)
2. Automatic retry with exponential backoff and jitter
3. Multiple authentication methods (Bearer, Basic, API Key, OAuth2)
4. Request/response middleware pipeline
5. Response caching with conditional requests
6. Rate limiting with sliding window
7. Circuit breaker pattern for fault tolerance
8. Comprehensive logging with request/response details
9. Timeout configuration (connect, read, total)
10. JSON/XML/Form data handling
11. File upload support with progress tracking
12. Mock server integration for testing
13. Async/await support
14. Performance monitoring and metrics

Make it extensible and include real-world usage examples."

RESULTADO DE COPILOT:
[Pega aquí el código generado por Copilot]

PROCESO DE REFINAMIENTO:
[Documenta aquí las mejoras que pediste a Copilot]

CÓDIGO FINAL:
"""
# Pega aquí el código final del cliente API


# DESAFÍO 4: Event-Driven Architecture System
"""
PROMPT PARA COPILOT AGENT:
"Implement a complete event-driven architecture system that includes:
1. Event bus with publish/subscribe pattern
2. Synchronous and asynchronous event handlers
3. Event priorities and execution ordering
4. Wildcard event subscriptions (e.g., 'user.*', 'order.*.created')
5. Event filtering with conditions and predicates
6. Event history and replay capabilities
7. Dead letter queue for failed events
8. Event persistence to disk/database
9. Distributed event handling across processes
10. Performance monitoring and metrics
11. Error handling and retry policies
12. Event transformation and enrichment
13. Real-time event streaming
14. Integration with external message queues

Include examples for e-commerce and user management scenarios."

RESULTADO DE COPILOT:
[Pega aquí el código generado por Copilot]

PROCESO DE REFINAMIENTO:
[Documenta aquí las mejoras que pediste a Copilot]

CÓDIGO FINAL:
"""
# Pega aquí el código final del sistema de eventos


# DESAFÍO 5: Database ORM with Query Builder
"""
PROMPT PARA COPILOT AGENT:
"Create a lightweight ORM (Object-Relational Mapping) system that features:
1. Model definition with field types and constraints
2. Database connection management with pooling
3. Fluent query builder with method chaining
4. CRUD operations (Create, Read, Update, Delete)
5. Advanced queries (joins, subqueries, aggregations)
6. Relationships (one-to-one, one-to-many, many-to-many)
7. Database migrations with version control
8. Transaction support with context managers
9. Raw SQL execution with parameter binding
10. Multiple database backend support (SQLite, PostgreSQL, MySQL)
11. Connection failover and load balancing
12. Query optimization and performance monitoring
13. Schema introspection and validation
14. Lazy loading and eager loading for relationships

Include examples for blog, e-commerce, and user management systems."

RESULTADO DE COPILOT:
[Pega aquí el código generado por Copilot]

PROCESO DE REFINAMIENTO:
[Documenta aquí las mejoras que pediste a Copilot]

CÓDIGO FINAL:
"""
# Pega aquí el código final del ORM


# DESAFÍO 6: Task Scheduler and Queue System
"""
PROMPT PARA COPILOT AGENT:
"Build a comprehensive task scheduling and queue system that supports:
1. Delayed task execution with precise timing
2. Recurring tasks with cron-like scheduling expressions
3. Task priorities and categories
4. Worker pool management with dynamic scaling
5. Task persistence and crash recovery
6. Progress tracking with callbacks and webhooks
7. Task dependencies and workflows
8. Error handling with exponential backoff retry
9. Dead letter queue for failed tasks
10. Real-time monitoring dashboard data
11. Task cancellation and modification
12. Distributed task execution across machines
13. Resource allocation and limits per task
14. Integration with external queue systems (Redis, RabbitMQ)

Include examples for data processing, email sending, and report generation."

RESULTADO DE COPILOT:
[Pega aquí el código generado por Copilot]

PROCESO DE REFINAMIENTO:
[Documenta aquí las mejoras que pediste a Copilot]

CÓDIGO FINAL:
"""
# Pega aquí el código final del sistema de tareas


# DESAFÍO 7: Configuration Management System
"""
PROMPT PARA COPILOT AGENT:
"Create an advanced configuration management system that provides:
1. Multiple configuration sources (JSON, YAML, TOML, environment variables, command line)
2. Hierarchical configuration with inheritance and overrides
3. Environment-specific configurations (dev, test, prod)
4. Configuration validation with JSON Schema
5. Hot reloading without application restart
6. Encrypted configuration values for secrets
7. Configuration templates with variable substitution
8. Default values and required field validation
9. Configuration versioning and rollback
10. Audit logging of configuration changes
11. Configuration distribution across services
12. Integration with external config stores (Consul, etcd)
13. Configuration diff and change detection
14. Type-safe configuration access

Include examples for microservices, web applications, and data pipelines."

RESULTADO DE COPILOT:
[Pega aquí el código generado por Copilot]

PROCESO DE REFINAMIENTO:
[Documenta aquí las mejoras que pediste a Copilot]

CÓDIGO FINAL:
"""
# Pega aquí el código final del sistema de configuración


# DESAFÍO 8: Testing and Mocking Framework
"""
PROMPT PARA COPILOT AGENT:
"Develop a testing and mocking framework that includes:
1. Fluent assertion library with readable error messages
2. Advanced mocking with behavior verification
3. Test data generation and fixtures
4. Test case organization with suites and categories
5. Parameterized tests with data providers
6. Test parallelization and isolation
7. Performance testing and benchmarking
8. Mock HTTP server with request recording
9. Database testing with transactions and rollback
10. Test reporting (HTML, JSON, JUnit XML)
11. Coverage analysis and reporting
12. Integration with CI/CD pipelines
13. Visual test comparison for UI testing
14. Load testing capabilities

Include examples for API testing, database testing, and performance testing."

RESULTADO DE COPILOT:
[Pega aquí el código generado por Copilot]

PROCESO DE REFINAMIENTO:
[Documenta aquí las mejoras que pediste a Copilot]

CÓDIGO FINAL:
"""
# Pega aquí el código final del framework de testing


# DESAFÍO 9: Monitoring and Observability System
"""
PROMPT PARA COPILOT AGENT:
"Create a comprehensive monitoring and observability system that features:
1. Metrics collection and aggregation
2. Distributed tracing across services
3. Structured logging with correlation IDs
4. Health checks and service discovery
5. Alerting with multiple notification channels
6. Performance profiling and bottleneck detection
7. Real-time dashboards and visualization
8. SLA/SLO monitoring and reporting
9. Error tracking and aggregation
10. Business metrics and KPI tracking
11. Integration with external monitoring systems (Prometheus, Grafana)
12. Anomaly detection using statistical methods
13. Capacity planning and forecasting
14. Incident management and response automation

Include examples for web applications, microservices, and data processing systems."

RESULTADO DE COPILOT:
[Pega aquí el código generado por Copilot]

PROCESO DE REFINAMIENTO:
[Documenta aquí las mejoras que pediste a Copilot]

CÓDIGO FINAL:
"""
# Pega aquí el código final del sistema de monitoreo


# DESAFÍO 10: Machine Learning Pipeline Framework
"""
PROMPT PARA COPILOT AGENT:
"Build a machine learning pipeline framework that supports:
1. Data ingestion from multiple sources (files, databases, APIs)
2. Data preprocessing and feature engineering
3. Model training with multiple algorithms
4. Hyperparameter tuning and optimization
5. Model validation and cross-validation
6. Model versioning and experiment tracking
7. Model deployment and serving
8. A/B testing for model comparison
9. Model monitoring and drift detection
10. Batch and real-time inference
11. Feature store for reusable features
12. Pipeline orchestration and scheduling
13. Resource management (CPU, GPU, memory)
14. Integration with popular ML libraries (scikit-learn, pandas, numpy)

Include examples for classification, regression, and recommendation systems."

RESULTADO DE COPILOT:
[Pega aquí el código generado por Copilot]

PROCESO DE REFINAMIENTO:
[Documenta aquí las mejoras que pediste a Copilot]

CÓDIGO FINAL:
"""
# Pega aquí el código final del framework de ML


if __name__ == "__main__":
    print("=== EJERCICIO 4: Copilot Agent ===")
    print("¡Desafía a Copilot Agent con sistemas complejos!")
    print("1. Copia cada prompt en Copilot Chat")
    print("2. Pega el código generado en las secciones correspondientes")
    print("3. Prueba y refina el código")
    print("4. Documenta tu experiencia")
    print("\nRecuerda: Copilot Agent es más efectivo con prompts detallados y específicos")
    print("No dudes en pedir mejoras y refinamientos al código generado")
    
    # Aquí puedes probar los sistemas que vayas implementando
    print("\n--- PRUEBAS DE SISTEMAS IMPLEMENTADOS ---")
    
    # Ejemplo: si implementaste el sistema de validación
    # validator = DataValidator()
    # result = validator.validate(data, schema)
    # print(f"Validación: {result}")
    
    print("¡Implementa los desafíos y prueba los sistemas generados por Copilot!")