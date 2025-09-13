"""
Ejemplos de uso de GitHub Copilot - Función Edit

Esta sesión práctica demuestra cómo usar GitHub Copilot para editar
y mejorar código Python existente.

Instrucciones para usar Copilot Edit:
1. Selecciona el código que quieres editar
2. Abre el panel de Copilot Chat (Ctrl+Shift+I)
3. Usa comandos como "/edit" seguido de tu instrucción
4. Prueba los comandos de ejemplo listados abajo

COMANDOS DE EDIT PARA PRACTICAR:

1. Refactoring:
   "/edit refactor this function to be more readable"
   "/edit split this function into smaller functions"
   "/edit improve the variable names"

2. Optimización:
   "/edit optimize this code for performance"
   "/edit make this more efficient"
   "/edit reduce the complexity of this algorithm"

3. Añadir funcionalidad:
   "/edit add error handling to this function"
   "/edit add logging to this code"
   "/edit add input validation"

4. Conversiones:
   "/edit convert this to use list comprehension"
   "/edit make this function async"
   "/edit add type hints to this code"
"""

import time
import logging
from typing import Any


# EJEMPLO 1: Función que necesita refactoring
def bad_function(data):
    """
    INSTRUCCIONES PARA EDIT:
    1. Selecciona esta función completa
    2. Usa: "/edit improve this function with better naming and structure"
    3. Usa: "/edit add type hints and docstring"
    4. Usa: "/edit add error handling"
    """
    result = []
    for i in data:
        if i > 0:
            x = i * 2
            if x > 10:
                y = x + 5
                result.append(y)
            else:
                result.append(x)
        else:
            result.append(0)
    return result


# EJEMPLO 2: Código que puede optimizarse
def inefficient_search(items, target):
    """
    INSTRUCCIONES PARA EDIT:
    1. Selecciona esta función
    2. Usa: "/edit optimize this search algorithm"
    3. Usa: "/edit make this more efficient using built-in functions"
    """
    found_items = []
    for i in range(len(items)):
        if items[i] == target:
            found_items.append(i)
    return found_items


# EJEMPLO 3: Función sin manejo de errores
def divide_numbers(a, b):
    """
    INSTRUCCIONES PARA EDIT:
    1. Selecciona esta función
    2. Usa: "/edit add proper error handling"
    3. Usa: "/edit add input validation"
    4. Usa: "/edit add comprehensive docstring"
    """
    return a / b


# EJEMPLO 4: Código repetitivo
def calculate_stats(numbers):
    """
    INSTRUCCIONES PARA EDIT:
    1. Selecciona esta función
    2. Usa: "/edit reduce code duplication"
    3. Usa: "/edit make this more maintainable"
    """
    if len(numbers) == 0:
        return None
    
    total = 0
    for num in numbers:
        total = total + num
    average = total / len(numbers)
    
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    
    return {
        'sum': total,
        'average': average,
        'max': max_val,
        'min': min_val
    }


# EJEMPLO 5: Clase que necesita mejoras
class UserManager:
    """
    INSTRUCCIONES PARA EDIT:
    1. Selecciona esta clase completa
    2. Usa: "/edit improve this class design"
    3. Usa: "/edit add proper error handling and validation"
    4. Usa: "/edit make this thread-safe"
    """
    
    def __init__(self):
        self.users = []
    
    def add_user(self, name, email):
        user = {'name': name, 'email': email, 'id': len(self.users)}
        self.users.append(user)
    
    def get_user(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None
    
    def delete_user(self, user_id):
        for i, user in enumerate(self.users):
            if user['id'] == user_id:
                del self.users[i]
                break


# EJEMPLO 6: Código sin logging
def process_file(filename):
    """
    INSTRUCCIONES PARA EDIT:
    1. Selecciona esta función
    2. Usa: "/edit add comprehensive logging"
    3. Usa: "/edit add progress tracking"
    4. Usa: "/edit make this more robust"
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    processed_lines = []
    for line in lines:
        line = line.strip()
        if line:
            line = line.upper()
            processed_lines.append(line)
    
    with open(filename.replace('.txt', '_processed.txt'), 'w') as f:
        for line in processed_lines:
            f.write(line + '\n')


# EJEMPLO 7: Función que necesita async
def fetch_multiple_urls(urls):
    """
    INSTRUCCIONES PARA EDIT:
    1. Selecciona esta función
    2. Usa: "/edit convert this to async/await"
    3. Usa: "/edit make this concurrent using asyncio"
    """
    import requests
    results = []
    for url in urls:
        try:
            response = requests.get(url)
            results.append(response.text)
        except Exception as e:
            results.append(f"Error: {str(e)}")
    return results


# EJEMPLO 8: Loop que puede ser comprehension
def filter_and_transform_data(data):
    """
    INSTRUCCIONES PARA EDIT:
    1. Selecciona esta función
    2. Usa: "/edit convert loops to list comprehensions"
    3. Usa: "/edit make this more pythonic"
    """
    positive_numbers = []
    for item in data:
        if isinstance(item, (int, float)) and item > 0:
            positive_numbers.append(item)
    
    squared_numbers = []
    for num in positive_numbers:
        squared_numbers.append(num ** 2)
    
    return squared_numbers


# EJEMPLO 9: Código sin type hints
def complex_function(data, config, processor):
    """
    INSTRUCCIONES PARA EDIT:
    1. Selecciona esta función
    2. Usa: "/edit add comprehensive type hints"
    3. Usa: "/edit improve parameter documentation"
    """
    if not data:
        return None
    
    if processor:
        processed_data = processor(data)
    else:
        processed_data = data
    
    if config.get('filter'):
        filtered_data = [item for item in processed_data if item > config['threshold']]
        return filtered_data
    
    return processed_data


# EJEMPLO 10: Función con lógica compleja
def validate_and_process_user_input(user_data):
    """
    INSTRUCCIONES PARA EDIT:
    1. Selecciona esta función
    2. Usa: "/edit split this into smaller, focused functions"
    3. Usa: "/edit improve readability and maintainability"
    """
    if not user_data or not isinstance(user_data, dict):
        return False, "Invalid input"
    
    if 'name' not in user_data or not user_data['name'] or len(user_data['name']) < 2:
        return False, "Name is required and must be at least 2 characters"
    
    if 'email' not in user_data or not user_data['email'] or '@' not in user_data['email']:
        return False, "Valid email is required"
    
    if 'age' not in user_data or not isinstance(user_data['age'], int) or user_data['age'] < 0 or user_data['age'] > 150:
        return False, "Valid age is required"
    
    processed_data = {
        'name': user_data['name'].strip().title(),
        'email': user_data['email'].strip().lower(),
        'age': user_data['age'],
        'created_at': time.time()
    }
    
    return True, processed_data


if __name__ == "__main__":
    print("=== Ejemplos para Copilot Edit ===")
    print("Selecciona el código y usa comandos /edit en Copilot Chat")
    print("Prueba diferentes tipos de refactoring y mejoras")
    
    # Ejemplos de uso que también puedes mejorar con Edit
    sample_data = [1, -2, 3, -4, 5, 6]
    print(f"Función con problemas: {bad_function(sample_data)}")
    
    numbers = [10, 5, 8, 3, 9, 1]
    print(f"Búsqueda ineficiente: {inefficient_search(numbers, 5)}")
    
    print(f"División: {divide_numbers(10, 2)}")
    
    stats = calculate_stats(numbers)
    print(f"Estadísticas: {stats}")