"""
EJERCICIO 2: Práctica con Copilot Ask

Objetivo: Usar Copilot Chat para analizar, explicar y mejorar código.

Instrucciones:
1. Abre el panel de Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Selecciona cada función/clase problemática
3. Haz las preguntas indicadas
4. Documenta las respuestas de Copilot
5. Implementa las mejoras sugeridas

PUNTUACIÓN:
- Pregunta realizada y documentada: 2 puntos
- Implementación de mejora sugerida: 3 puntos
- Total posible: 50 puntos
"""

import time
import requests
from typing import List, Dict, Any


# CÓDIGO PROBLEMÁTICO 1: Función ineficiente
def slow_search(data: List[int], target: int) -> List[int]:
    """
    Función con problemas de rendimiento.
    
    PREGUNTAS PARA COPILOT:
    1. "¿Qué problemas de rendimiento tiene esta función?"
    2. "¿Cómo puedo optimizar esta búsqueda?"
    3. "¿Cuál es la complejidad temporal de este algoritmo?"
    
    RESPUESTAS DE COPILOT:
    1. [Escribe aquí la respuesta de Copilot]
    
    2. [Escribe aquí la respuesta de Copilot]
    
    3. [Escribe aquí la respuesta de Copilot]
    """
    results = []
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j and data[i] == target:
                results.append(i)
    return results

# IMPLEMENTA AQUÍ LA VERSIÓN MEJORADA:
def optimized_search(data: List[int], target: int) -> List[int]:
    """Versión optimizada basada en sugerencias de Copilot"""
    # TODO: Implementar la versión mejorada
    pass


# CÓDIGO PROBLEMÁTICO 2: Manejo de archivos inseguro
def read_config_file(filename: str) -> dict:
    """
    Función con problemas de manejo de archivos.
    
    PREGUNTAS PARA COPILOT:
    1. "¿Qué problemas tiene esta función para manejar archivos?"
    2. "¿Cómo debería manejar los errores de archivo en Python?"
    3. "¿Qué es un context manager y por qué debería usarlo?"
    
    RESPUESTAS DE COPILOT:
    1. [Escribe aquí la respuesta de Copilot]
    
    2. [Escribe aquí la respuesta de Copilot]
    
    3. [Escribe aquí la respuesta de Copilot]
    """
    import json
    file = open(filename, 'r')
    data = json.load(file)
    file.close()
    return data

# IMPLEMENTA AQUÍ LA VERSIÓN MEJORADA:
def safe_read_config_file(filename: str) -> dict:
    """Versión segura basada en sugerencias de Copilot"""
    # TODO: Implementar la versión mejorada
    pass


# CÓDIGO PROBLEMÁTICO 3: Clase mal diseñada
class DataProcessor:
    """
    Clase con problemas de diseño.
    
    PREGUNTAS PARA COPILOT:
    1. "¿Qué problemas de diseño tiene esta clase?"
    2. "¿Cómo puedo aplicar el principio de responsabilidad única aquí?"
    3. "¿Qué patrones de diseño podrían mejorar esta clase?"
    
    RESPUESTAS DE COPILOT:
    1. [Escribe aquí la respuesta de Copilot]
    
    2. [Escribe aquí la respuesta de Copilot]
    
    3. [Escribe aquí la respuesta de Copilot]
    """
    
    def __init__(self):
        self.data = []
        self.processed_data = []
        self.db_connection = None
        self.api_client = None
        self.logger = None
    
    def process_everything(self, input_data, db_config, api_config):
        # Esta función hace demasiadas cosas
        self.data = input_data
        self.connect_to_database(db_config)
        self.setup_api_client(api_config)
        self.validate_data()
        self.clean_data()
        self.transform_data()
        self.save_to_database()
        self.send_to_api()
        self.generate_report()
        return self.processed_data
    
    def connect_to_database(self, config):
        # Simulación de conexión a BD
        pass
    
    def setup_api_client(self, config):
        # Configuración de cliente API
        pass
    
    def validate_data(self):
        # Validación de datos
        pass
    
    def clean_data(self):
        # Limpieza de datos
        pass
    
    def transform_data(self):
        # Transformación de datos
        pass
    
    def save_to_database(self):
        # Guardado en BD
        pass
    
    def send_to_api(self):
        # Envío a API
        pass
    
    def generate_report(self):
        # Generación de reporte
        pass

# IMPLEMENTA AQUÍ LAS CLASES MEJORADAS:
class ImprovedDataProcessor:
    """Versión mejorada basada en sugerencias de Copilot"""
    # TODO: Implementar el diseño mejorado
    pass


# CÓDIGO PROBLEMÁTICO 4: Función con lógica compleja
def calculate_discount(customer_type, purchase_amount, items_count, is_member, purchase_date):
    """
    Función con lógica de negocio compleja y difícil de mantener.
    
    PREGUNTAS PARA COPILOT:
    1. "¿Cómo puedo refactorizar esta función para que sea más legible?"
    2. "¿Debería dividir esta función en funciones más pequeñas?"
    3. "¿Cómo puedo hacer esta lógica más mantenible y testeable?"
    
    RESPUESTAS DE COPILOT:
    1. [Escribe aquí la respuesta de Copilot]
    
    2. [Escribe aquí la respuesta de Copilot]
    
    3. [Escribe aquí la respuesta de Copilot]
    """
    discount = 0
    
    if customer_type == "premium":
        if purchase_amount > 1000:
            discount = 0.15
        elif purchase_amount > 500:
            discount = 0.10
        else:
            discount = 0.05
    elif customer_type == "regular":
        if is_member:
            if purchase_amount > 200:
                discount = 0.08
            else:
                discount = 0.03
        else:
            if purchase_amount > 100:
                discount = 0.05
    
    if items_count > 10:
        discount += 0.02
    
    import datetime
    if purchase_date.month == 12:  # Descuento navideño
        discount += 0.05
    
    if purchase_date.weekday() == 0:  # Descuento de lunes
        discount += 0.03
    
    return min(discount, 0.30)  # Máximo 30% de descuento

# IMPLEMENTA AQUÍ LA VERSIÓN MEJORADA:
def improved_calculate_discount(customer_type, purchase_amount, items_count, is_member, purchase_date):
    """Versión mejorada basada en sugerencias de Copilot"""
    # TODO: Implementar la versión refactorizada
    pass


# CÓDIGO PROBLEMÁTICO 5: Función con problemas de seguridad
def execute_user_query(query: str, database_name: str) -> str:
    """
    Función con vulnerabilidades de seguridad.
    
    PREGUNTAS PARA COPILOT:
    1. "¿Qué vulnerabilidades de seguridad tiene esta función?"
    2. "¿Cómo puedo prevenir ataques de SQL injection?"
    3. "¿Qué otras medidas de seguridad debería implementar?"
    
    RESPUESTAS DE COPILOT:
    1. [Escribe aquí la respuesta de Copilot]
    
    2. [Escribe aquí la respuesta de Copilot]
    
    3. [Escribe aquí la respuesta de Copilot]
    """
    import sqlite3
    
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    # ¡Vulnerabilidad de SQL Injection!
    full_query = f"SELECT * FROM users WHERE {query}"
    cursor.execute(full_query)
    
    results = cursor.fetchall()
    conn.close()
    
    return str(results)

# IMPLEMENTA AQUÍ LA VERSIÓN SEGURA:
def secure_execute_user_query(query_params: Dict[str, Any], database_name: str) -> List[Dict]:
    """Versión segura basada en sugerencias de Copilot"""
    # TODO: Implementar la versión segura
    pass


if __name__ == "__main__":
    print("=== EJERCICIO 2: Copilot Ask ===")
    print("1. Selecciona cada función problemática")
    print("2. Haz las preguntas indicadas a Copilot")
    print("3. Documenta las respuestas")
    print("4. Implementa las mejoras sugeridas")
    print("5. Compara el rendimiento y calidad del código original vs mejorado")
    
    # Datos de prueba
    test_data = [1, 2, 3, 2, 4, 2, 5]
    print(f"Datos de prueba: {test_data}")
    
    # Prueba función lenta
    start = time.time()
    slow_result = slow_search(test_data, 2)
    slow_time = time.time() - start
    print(f"Búsqueda lenta: {slow_result} (tiempo: {slow_time:.4f}s)")
    
    # TODO: Añadir pruebas de las funciones mejoradas