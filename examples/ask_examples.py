"""
Ejemplos de uso de GitHub Copilot - Función Ask

Esta sesión práctica demuestra cómo hacer preguntas a GitHub Copilot
para obtener ayuda con tu código Python.

Instrucciones para usar Copilot Ask:
1. Abre el panel de Copilot Chat (Ctrl+Shift+I o Cmd+Shift+I)
2. Haz preguntas específicas sobre el código
3. Prueba los diferentes tipos de preguntas listados abajo

PREGUNTAS DE EJEMPLO PARA PRACTICAR:

1. Preguntas sobre explicación de código:
   "¿Qué hace esta función?"
   "¿Cómo funciona este algoritmo?"
   "Explica esta línea de código"

2. Preguntas sobre mejoras:
   "¿Cómo puedo optimizar esta función?"
   "¿Hay una forma más eficiente de hacer esto?"
   "¿Cómo puedo hacer este código más legible?"

3. Preguntas sobre debugging:
   "¿Por qué mi código no funciona?"
   "¿Cuál podría ser el error aquí?"
   "¿Cómo puedo depurar esta función?"

4. Preguntas sobre best practices:
   "¿Es este código pythónico?"
   "¿Qué mejores prácticas debería seguir?"
   "¿Cómo puedo manejar errores aquí?"
"""

import requests
import json
from typing import List, Dict, Optional
import pandas as pd


def fetch_user_data(user_id: int) -> Optional[Dict]:
    """
    Obtiene datos de usuario desde una API.
    
    PREGUNTA PARA COPILOT:
    "¿Cómo puedo mejorar el manejo de errores en esta función?"
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def complex_calculation(numbers: List[float]) -> float:
    """
    Realiza un cálculo complejo con una lista de números.
    
    PREGUNTAS PARA COPILOT:
    "¿Qué hace exactamente esta función?"
    "¿Hay algún problema con esta implementación?"
    "¿Cómo puedo optimizar este código?"
    """
    result = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                result += numbers[i] / (numbers[j] + 1)
    return result


def process_data_frame(df: pd.DataFrame) -> pd.DataFrame:
    """
    Procesa un DataFrame de pandas de manera poco eficiente.
    
    PREGUNTAS PARA COPILOT:
    "¿Cómo puedo hacer este código más eficiente?"
    "¿Qué mejores prácticas de pandas debería usar?"
    "¿Hay funciones vectorizadas que pueda usar aquí?"
    """
    new_data = []
    for index, row in df.iterrows():
        new_row = {}
        for col in df.columns:
            if isinstance(row[col], str):
                new_row[col] = row[col].upper()
            elif isinstance(row[col], (int, float)):
                new_row[col] = row[col] * 2
            else:
                new_row[col] = row[col]
        new_data.append(new_row)
    return pd.DataFrame(new_data)


class DataProcessor:
    """
    Una clase para procesar datos con algunos problemas de diseño.
    
    PREGUNTAS PARA COPILOT:
    "¿Cómo puedo mejorar el diseño de esta clase?"
    "¿Qué patrones de diseño podría aplicar aquí?"
    "¿Cómo puedo hacer esta clase más reutilizable?"
    """
    
    def __init__(self):
        self.data = []
        self.processed_data = []
        self.config = {
            'multiplier': 2,
            'filter_threshold': 10,
            'output_format': 'json'
        }
    
    def load_data(self, data):
        self.data = data
    
    def process(self):
        for item in self.data:
            if item > self.config['filter_threshold']:
                processed_item = item * self.config['multiplier']
                self.processed_data.append(processed_item)
    
    def get_results(self):
        if self.config['output_format'] == 'json':
            return json.dumps(self.processed_data)
        return self.processed_data


def recursive_function(n: int) -> int:
    """
    Una función recursiva sin caso base claro.
    
    PREGUNTAS PARA COPILOT:
    "¿Hay algún problema con esta función recursiva?"
    "¿Cómo puedo evitar el stack overflow?"
    "¿Qué está mal con esta implementación?"
    """
    if n > 0:
        return n + recursive_function(n - 1)
    # Falta el caso base explícito


def file_operations(filename: str) -> str:
    """
    Operaciones de archivo sin manejo adecuado de errores.
    
    PREGUNTAS PARA COPILOT:
    "¿Cómo debería manejar los errores de archivo aquí?"
    "¿Qué pasa si el archivo no existe?"
    "¿Cómo puedo hacer este código más robusto?"
    """
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content.upper()


def security_issue(user_input: str) -> str:
    """
    Una función con potenciales problemas de seguridad.
    
    PREGUNTAS PARA COPILOT:
    "¿Hay algún problema de seguridad en este código?"
    "¿Cómo puedo validar la entrada del usuario?"
    "¿Qué vulnerabilidades podría tener esta función?"
    """
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    return query


# EJERCICIOS PARA PRACTICAR CON COPILOT ASK:

"""
EJERCICIO 1: Análisis de código
Selecciona la función fetch_user_data y pregunta:
- "¿Qué hace esta función?"
- "¿Cómo puedo mejorar el manejo de errores?"
- "¿Debería usar async/await aquí?"

EJERCICIO 2: Optimización
Selecciona complex_calculation y pregunta:
- "¿Es eficiente esta función?"
- "¿Cómo puedo optimizarla?"
- "¿Qué complejidad temporal tiene?"

EJERCICIO 3: Best Practices
Selecciona file_operations y pregunta:
- "¿Qué está mal con este código?"
- "¿Cómo debería manejar archivos en Python?"
- "¿Debería usar context managers aquí?"

EJERCICIO 4: Seguridad
Selecciona security_issue y pregunta:
- "¿Es segura esta función?"
- "¿Cómo puedo prevenir SQL injection?"
- "¿Qué validaciones debería añadir?"

EJERCICIO 5: Diseño
Selecciona la clase DataProcessor y pregunta:
- "¿Cómo puedo mejorar este diseño?"
- "¿Debería usar herencia o composición?"
- "¿Qué patrones de diseño aplicarías?"
"""


if __name__ == "__main__":
    print("=== Ejemplos para Copilot Ask ===")
    print("Abre el panel de Copilot Chat y haz preguntas sobre este código")
    print("Selecciona funciones específicas y pregunta sobre ellas")
    
    # Prueba algunas funciones para generar preguntas
    sample_data = [1, 2, 3, 4, 5]
    print(f"Resultado del cálculo complejo: {complex_calculation(sample_data)}")
    
    processor = DataProcessor()
    processor.load_data([5, 15, 25, 35])
    processor.process()
    print(f"Datos procesados: {processor.get_results()}")