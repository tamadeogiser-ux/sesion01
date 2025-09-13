"""
Funciones de utilidad para la sesión práctica de GitHub Copilot.
"""

import time
import functools
import json
from typing import Any, Callable, Dict, List


def timer_decorator(func: Callable) -> Callable:
    """
    Decorador para medir el tiempo de ejecución de funciones.
    Útil para practicar con Copilot en análisis de rendimiento.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ejecutada en {end_time - start_time:.4f} segundos")
        return result
    return wrapper


def validate_email(email: str) -> bool:
    """
    Validación básica de email para ejemplos.
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def safe_divide(a: float, b: float) -> float:
    """
    División segura que maneja división por cero.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')


def load_json_safely(filename: str) -> Dict[str, Any]:
    """
    Carga un archivo JSON de manera segura.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Archivo {filename} no encontrado")
        return {}
    except json.JSONDecodeError:
        print(f"Error al decodificar JSON en {filename}")
        return {}


def create_sample_data() -> List[Dict[str, Any]]:
    """
    Crea datos de ejemplo para practicar con Copilot.
    """
    return [
        {"name": "Alice", "age": 30, "email": "alice@example.com", "score": 85},
        {"name": "Bob", "age": 25, "email": "bob@example.com", "score": 92},
        {"name": "Charlie", "age": 35, "email": "charlie@example.com", "score": 78},
        {"name": "Diana", "age": 28, "email": "diana@example.com", "score": 95},
        {"name": "Eve", "age": 32, "email": "eve@example.com", "score": 88}
    ]


class Logger:
    """
    Logger simple para ejemplos de Copilot.
    """
    
    def __init__(self, name: str = "CopilotSession"):
        self.name = name
        self.logs = []
    
    def info(self, message: str):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] INFO - {self.name}: {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def error(self, message: str):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] ERROR - {self.name}: {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def get_logs(self) -> List[str]:
        return self.logs.copy()


def format_currency(amount: float, currency: str = "USD") -> str:
    """
    Formatea una cantidad como moneda.
    """
    symbols = {
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥"
    }
    symbol = symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f}"


def chunks(lst: List[Any], n: int) -> List[List[Any]]:
    """
    Divide una lista en chunks de tamaño n.
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]