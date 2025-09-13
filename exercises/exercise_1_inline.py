"""
EJERCICIO 1: Práctica con Copilot Inline

Objetivo: Completar las siguientes funciones usando las sugerencias inline de Copilot.

Instrucciones:
1. Coloca el cursor después de cada comentario "# TODO:"
2. Comienza a escribir el código
3. Observa y acepta las sugerencias de Copilot con Tab
4. Si la sugerencia no es correcta, presiona Esc y continúa escribiendo

PUNTUACIÓN:
- Función completada correctamente: 2 puntos
- Uso efectivo de sugerencias Copilot: 1 punto
- Total posible: 30 puntos
"""

from typing import List, Dict
import math


def calculate_bmi(weight: float, height: float) -> float:
    """
    Calcula el Índice de Masa Corporal (BMI).
    
    Args:
        weight: Peso en kilogramos
        height: Altura en metros
    
    Returns:
        BMI calculado
    """
    # TODO: Implementar cálculo de BMI (peso / altura^2)


def find_prime_numbers(limit: int) -> List[int]:
    """
    Encuentra todos los números primos hasta el límite dado.
    
    Args:
        limit: Número límite (exclusivo)
    
    Returns:
        Lista de números primos
    """
    # TODO: Implementar algoritmo para encontrar números primos


def reverse_words_in_sentence(sentence: str) -> str:
    """
    Invierte el orden de las palabras en una oración.
    
    Args:
        sentence: Oración original
    
    Returns:
        Oración con palabras invertidas
    """
    # TODO: Invertir el orden de las palabras


def calculate_compound_interest(principal: float, rate: float, time: int, compound_frequency: int = 1) -> float:
    """
    Calcula el interés compuesto.
    
    Args:
        principal: Cantidad principal
        rate: Tasa de interés anual (como decimal)
        time: Tiempo en años
        compound_frequency: Frecuencia de capitalización por año
    
    Returns:
        Monto final con interés compuesto
    """
    # TODO: Implementar fórmula de interés compuesto


def find_most_frequent_word(text: str) -> str:
    """
    Encuentra la palabra más frecuente en un texto.
    
    Args:
        text: Texto a analizar
    
    Returns:
        La palabra más frecuente
    """
    # TODO: Encontrar la palabra más frecuente


def validate_password_strength(password: str) -> Dict[str, bool]:
    """
    Valida la fortaleza de una contraseña.
    
    Args:
        password: Contraseña a validar
    
    Returns:
        Diccionario con criterios de validación
    """
    # TODO: Implementar validación de contraseña
    # Criterios: longitud >= 8, mayúscula, minúscula, número, carácter especial


def convert_temperature(temp: float, from_unit: str, to_unit: str) -> float:
    """
    Convierte temperatura entre diferentes unidades.
    
    Args:
        temp: Temperatura a convertir
        from_unit: Unidad origen ('C', 'F', 'K')
        to_unit: Unidad destino ('C', 'F', 'K')
    
    Returns:
        Temperatura convertida
    """
    # TODO: Implementar conversión de temperatura


def generate_fibonacci_sequence(n: int) -> List[int]:
    """
    Genera la secuencia de Fibonacci hasta n términos.
    
    Args:
        n: Número de términos a generar
    
    Returns:
        Lista con la secuencia de Fibonacci
    """
    # TODO: Generar secuencia de Fibonacci


def calculate_distance_between_points(point1: tuple, point2: tuple) -> float:
    """
    Calcula la distancia euclidiana entre dos puntos.
    
    Args:
        point1: Primera coordenada (x, y)
        point2: Segunda coordenada (x, y)
    
    Returns:
        Distancia entre los puntos
    """
    # TODO: Implementar fórmula de distancia euclidiana


def sort_students_by_grade(students: List[Dict[str, any]]) -> List[Dict[str, any]]:
    """
    Ordena estudiantes por calificación de mayor a menor.
    
    Args:
        students: Lista de diccionarios con datos de estudiantes
                 Formato: [{'name': 'Juan', 'grade': 85}, ...]
    
    Returns:
        Lista ordenada de estudiantes
    """
    # TODO: Ordenar estudiantes por calificación


# TESTS PARA VERIFICAR TUS IMPLEMENTACIONES
if __name__ == "__main__":
    print("=== EJERCICIO 1: Copilot Inline ===")
    
    # Test BMI
    try:
        bmi = calculate_bmi(70, 1.75)
        print(f"BMI (70kg, 1.75m): {bmi:.2f}")
        assert 22 < bmi < 23, "BMI incorrecto"
        print("✓ BMI test pasado")
    except Exception as e:
        print(f"✗ Error en BMI: {e}")
    
    # Test primos
    try:
        primes = find_prime_numbers(20)
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19]
        print(f"Primos hasta 20: {primes}")
        assert primes == expected_primes, "Números primos incorrectos"
        print("✓ Primos test pasado")
    except Exception as e:
        print(f"✗ Error en primos: {e}")
    
    # Test inversión de palabras
    try:
        reversed_sentence = reverse_words_in_sentence("Hola mundo Python")
        print(f"Palabras invertidas: {reversed_sentence}")
        assert reversed_sentence == "Python mundo Hola", "Inversión incorrecta"
        print("✓ Inversión test pasado")
    except Exception as e:
        print(f"✗ Error en inversión: {e}")
    
    # Test temperatura
    try:
        celsius_to_fahrenheit = convert_temperature(0, 'C', 'F')
        print(f"0°C a Fahrenheit: {celsius_to_fahrenheit}")
        assert abs(celsius_to_fahrenheit - 32) < 0.01, "Conversión incorrecta"
        print("✓ Temperatura test pasado")
    except Exception as e:
        print(f"✗ Error en temperatura: {e}")
    
    print("\n¡Completa todas las funciones y ejecuta los tests!")