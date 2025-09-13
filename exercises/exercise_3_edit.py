"""
EJERCICIO 3: Práctica con Copilot Edit

Objetivo: Usar los comandos /edit de Copilot para refactorizar y mejorar código existente.

Instrucciones:
1. Selecciona el código a editar
2. Abre Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
3. Usa los comandos /edit listados para cada sección
4. Aplica las sugerencias de Copilot
5. Compara el código antes y después

PUNTUACIÓN:
- Comando /edit usado correctamente: 2 puntos
- Mejora aplicada exitosamente: 3 puntos
- Total posible: 50 puntos
"""

from typing import List, Dict, Any, Optional
import json
import time


# SECCIÓN 1: Función con nombres de variables pobres
def func1(x, y, z):
    """
    COMANDO PARA COPILOT:
    Selecciona esta función y usa:
    "/edit improve variable names and add type hints"
    
    ANTES DE EDIT:
    [Pega aquí el código original]
    
    DESPUÉS DE EDIT:
    [Pega aquí el código mejorado por Copilot]
    """
    result = []
    for i in x:
        if i > y:
            temp = i * z
            result.append(temp)
    return result


# SECCIÓN 2: Código repetitivo que necesita DRY (Don't Repeat Yourself)
def process_users():
    """
    COMANDO PARA COPILOT:
    Selecciona esta función y usa:
    "/edit refactor to eliminate code duplication using DRY principles"
    
    ANTES DE EDIT:
    [Pega aquí el código original]
    
    DESPUÉS DE EDIT:
    [Pega aquí el código mejorado por Copilot]
    """
    # Procesamiento de usuarios activos
    active_users = []
    for user in get_all_users():
        if user['status'] == 'active':
            user['processed'] = True
            user['timestamp'] = time.time()
            user['category'] = 'processed_active'
            active_users.append(user)
    
    # Procesamiento de usuarios inactivos
    inactive_users = []
    for user in get_all_users():
        if user['status'] == 'inactive':
            user['processed'] = True
            user['timestamp'] = time.time()
            user['category'] = 'processed_inactive'
            inactive_users.append(user)
    
    # Procesamiento de usuarios pendientes
    pending_users = []
    for user in get_all_users():
        if user['status'] == 'pending':
            user['processed'] = True
            user['timestamp'] = time.time()
            user['category'] = 'processed_pending'
            pending_users.append(user)
    
    return active_users, inactive_users, pending_users


def get_all_users():
    """Función auxiliar que simula obtener usuarios"""
    return [
        {'id': 1, 'name': 'Juan', 'status': 'active'},
        {'id': 2, 'name': 'María', 'status': 'inactive'},
        {'id': 3, 'name': 'Pedro', 'status': 'pending'},
    ]


# SECCIÓN 3: Loops que pueden ser list comprehensions
def filter_and_transform_data(data_list):
    """
    COMANDO PARA COPILOT:
    Selecciona esta función y usa:
    "/edit convert loops to list comprehensions where appropriate"
    
    ANTES DE EDIT:
    [Pega aquí el código original]
    
    DESPUÉS DE EDIT:
    [Pega aquí el código mejorado por Copilot]
    """
    # Filtrar números positivos
    positive_numbers = []
    for num in data_list:
        if isinstance(num, (int, float)) and num > 0:
            positive_numbers.append(num)
    
    # Elevar al cuadrado
    squared_numbers = []
    for num in positive_numbers:
        squared_numbers.append(num ** 2)
    
    # Convertir a strings
    string_numbers = []
    for num in squared_numbers:
        string_numbers.append(str(num))
    
    # Filtrar solo los que tienen menos de 3 dígitos
    short_strings = []
    for s in string_numbers:
        if len(s) < 3:
            short_strings.append(s)
    
    return short_strings


# SECCIÓN 4: Función sin manejo de errores
def divide_and_process(numbers, divisor):
    """
    COMANDO PARA COPILOT:
    Selecciona esta función y usa:
    "/edit add comprehensive error handling and input validation"
    
    ANTES DE EDIT:
    [Pega aquí el código original]
    
    DESPUÉS DE EDIT:
    [Pega aquí el código mejorado por Copilot]
    """
    results = []
    for num in numbers:
        divided = num / divisor
        processed = divided * 2 + 5
        results.append(processed)
    
    return results


# SECCIÓN 5: Clase con métodos demasiado largos
class DataAnalyzer:
    """
    COMANDO PARA COPILOT:
    Selecciona esta clase completa y usa:
    "/edit split long methods into smaller, focused methods"
    
    ANTES DE EDIT:
    [Pega aquí el código original]
    
    DESPUÉS DE EDIT:
    [Pega aquí el código mejorado por Copilot]
    """
    
    def __init__(self):
        self.data = []
        self.results = {}
    
    def analyze_comprehensive_data(self, data_input):
        # Validación de entrada
        if not data_input:
            return None
        if not isinstance(data_input, list):
            return None
        
        # Limpieza de datos
        cleaned_data = []
        for item in data_input:
            if isinstance(item, dict):
                if 'value' in item and isinstance(item['value'], (int, float)):
                    if item['value'] >= 0:
                        cleaned_item = {
                            'value': item['value'],
                            'category': item.get('category', 'unknown'),
                            'timestamp': item.get('timestamp', time.time())
                        }
                        cleaned_data.append(cleaned_item)
        
        # Análisis estadístico
        if not cleaned_data:
            return None
        
        values = [item['value'] for item in cleaned_data]
        total = sum(values)
        average = total / len(values)
        maximum = max(values)
        minimum = min(values)
        
        # Análisis por categorías
        categories = {}
        for item in cleaned_data:
            cat = item['category']
            if cat not in categories:
                categories[cat] = {'count': 0, 'total': 0, 'items': []}
            categories[cat]['count'] += 1
            categories[cat]['total'] += item['value']
            categories[cat]['items'].append(item)
        
        # Cálculos adicionales por categoría
        for cat in categories:
            categories[cat]['average'] = categories[cat]['total'] / categories[cat]['count']
            categories[cat]['percentage'] = (categories[cat]['count'] / len(cleaned_data)) * 100
        
        # Generación del reporte final
        self.results = {
            'total_items': len(cleaned_data),
            'statistics': {
                'sum': total,
                'average': average,
                'max': maximum,
                'min': minimum
            },
            'categories': categories,
            'processed_at': time.time()
        }
        
        return self.results


# SECCIÓN 6: Función con lógica condicional compleja
def determine_shipping_cost(weight, destination, is_express, is_fragile, customer_type):
    """
    COMANDO PARA COPILOT:
    Selecciona esta función y usa:
    "/edit simplify complex conditional logic and improve readability"
    
    ANTES DE EDIT:
    [Pega aquí el código original]
    
    DESPUÉS DE EDIT:
    [Pega aquí el código mejorado por Copilot]
    """
    base_cost = 0
    
    if weight <= 1:
        base_cost = 5
    elif weight <= 5:
        base_cost = 10
    elif weight <= 10:
        base_cost = 20
    else:
        base_cost = 30
    
    if destination == 'local':
        multiplier = 1.0
    elif destination == 'national':
        multiplier = 1.5
    elif destination == 'international':
        multiplier = 3.0
    else:
        multiplier = 1.0
    
    if is_express:
        if destination == 'local':
            multiplier += 0.5
        elif destination == 'national':
            multiplier += 1.0
        else:
            multiplier += 2.0
    
    if is_fragile:
        if weight > 5:
            multiplier += 1.0
        else:
            multiplier += 0.5
    
    if customer_type == 'premium':
        multiplier *= 0.9
    elif customer_type == 'vip':
        multiplier *= 0.8
    elif customer_type == 'new':
        multiplier *= 1.1
    
    final_cost = base_cost * multiplier
    
    if final_cost < 5:
        final_cost = 5
    
    return round(final_cost, 2)


# SECCIÓN 7: Función sin type hints ni documentación
def process_json_data(data, config, transformations):
    """
    COMANDO PARA COPILOT:
    Selecciona esta función y usa:
    "/edit add comprehensive type hints and detailed docstring"
    
    ANTES DE EDIT:
    [Pega aquí el código original]
    
    DESPUÉS DE EDIT:
    [Pega aquí el código mejorado por Copilot]
    """
    if not data:
        return None
    
    result = {}
    for key, value in data.items():
        if key in config:
            if config[key]['enabled']:
                transformed_value = value
                for transform in transformations.get(key, []):
                    if transform == 'upper':
                        transformed_value = transformed_value.upper()
                    elif transform == 'strip':
                        transformed_value = transformed_value.strip()
                    elif transform == 'int':
                        transformed_value = int(transformed_value)
                result[key] = transformed_value
    
    return result


# SECCIÓN 8: Código con magic numbers y strings
def calculate_grade(score):
    """
    COMANDO PARA COPILOT:
    Selecciona esta función y usa:
    "/edit replace magic numbers with named constants and improve maintainability"
    
    ANTES DE EDIT:
    [Pega aquí el código original]
    
    DESPUÉS DE EDIT:
    [Pega aquí el código mejorado por Copilot]
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


if __name__ == "__main__":
    print("=== EJERCICIO 3: Copilot Edit ===")
    print("1. Selecciona cada sección de código")
    print("2. Usa los comandos /edit indicados en Copilot Chat")
    print("3. Aplica las mejoras sugeridas")
    print("4. Documenta los cambios realizados")
    
    # Pruebas del código original
    test_data = [-2, 1, 3, 5, 7, 9]
    print(f"Datos de prueba: {test_data}")
    
    # Prueba func1 original
    result1 = func1(test_data, 2, 1.5)
    print(f"Función 1 resultado: {result1}")
    
    # Prueba filter_and_transform_data original
    result2 = filter_and_transform_data(test_data)
    print(f"Filtro y transformación: {result2}")
    
    print("\n¡Usa /edit para mejorar cada función y compara los resultados!")