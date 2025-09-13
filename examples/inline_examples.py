"""
Ejemplos de uso de GitHub Copilot - Función Inline

Esta sesión práctica demuestra cómo usar las sugerencias inline de GitHub Copilot
mientras escribes código Python.

Instrucciones:
1. Abre este archivo en VS Code con GitHub Copilot activado
2. Coloca el cursor al final de cada función incompleta
3. Comienza a escribir y observa las sugerencias inline de Copilot
4. Acepta las sugerencias con Tab o recházalas con Esc
"""

import math
import datetime
from typing import List, Dict


def calculate_circle_area(radius: float) -> float:
    """
    Calcula el área de un círculo dado su radio.
    
    Ejercicio: Coloca el cursor después de los dos puntos y comienza a escribir
    Copilot debería sugerir: return math.pi * radius ** 2
    """
    # Escribe aquí la implementación


def generate_fibonacci(n: int) -> List[int]:
    """
    Genera una secuencia de Fibonacci con n elementos.
    
    Ejercicio: Copilot puede ayudarte a implementar la secuencia de Fibonacci
    """
    # Escribe aquí la implementación


def is_prime(number: int) -> bool:
    """
    Determina si un número es primo.
    
    Ejercicio: Copilot puede sugerir una implementación eficiente
    """
    # Escribe aquí la implementación


def format_currency(amount: float, currency: str = "USD") -> str:
    """
    Formatea una cantidad como moneda.
    
    Ejercicio: Copilot puede ayudar con el formato de moneda
    """
    # Escribe aquí la implementación


def get_current_timestamp() -> str:
    """
    Obtiene el timestamp actual en formato ISO.
    
    Ejercicio: Copilot puede sugerir el uso de datetime
    """
    # Escribe aquí la implementación


def validate_email(email: str) -> bool:
    """
    Valida si una dirección de email es válida usando regex.
    
    Ejercicio: Copilot puede ayudar con el patrón de regex
    """
    import re
    # Escribe aquí la implementación


def create_user_dict(name: str, age: int, email: str) -> Dict[str, any]:
    """
    Crea un diccionario de usuario con validaciones.
    
    Ejercicio: Copilot puede sugerir validaciones y estructura del diccionario
    """
    # Escribe aquí la implementación


def sort_by_length(words: List[str]) -> List[str]:
    """
    Ordena una lista de palabras por longitud.
    
    Ejercicio: Copilot puede sugerir el uso de sorted() con key
    """
    # Escribe aquí la implementación


def count_word_frequency(text: str) -> Dict[str, int]:
    """
    Cuenta la frecuencia de palabras en un texto.
    
    Ejercicio: Copilot puede ayudar con el conteo y limpieza del texto
    """
    # Escribe aquí la implementación


class Calculator:
    """
    Una clase calculadora simple.
    
    Ejercicio: Copilot puede ayudar a implementar métodos de la clase
    """
    
    def __init__(self):
        # Escribe aquí la inicialización
        pass
    
    def add(self, a: float, b: float) -> float:
        # Escribe aquí la implementación
        pass
    
    def multiply(self, a: float, b: float) -> float:
        # Escribe aquí la implementación
        pass
    
    def divide(self, a: float, b: float) -> float:
        # Escribe aquí la implementación (considera división por cero)
        pass


if __name__ == "__main__":
    # Ejemplos de uso - Copilot puede ayudar a completar estos ejemplos
    print("=== Ejemplos de Copilot Inline ===")
    
    # Prueba las funciones aquí
    # Copilot puede sugerir llamadas de función y casos de prueba