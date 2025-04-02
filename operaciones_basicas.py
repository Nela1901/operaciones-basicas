"""Módulo que contiene clases para operaciones básicas y cálculo de promedios."""

class OperacionesBasicas:
    """Clase para realizar operaciones matemáticas básicas."""

    def __init__(self):
        self._resultado = 0

    def sumar(self, a, b):
        """Suma dos números y guarda el resultado."""
        self._resultado = a + b

    def restar(self, a, b):
        """Resta dos números y guarda el resultado."""
        self._resultado = a - b

    @property
    def resultado(self):
        """Devuelve el resultado de la última operación."""
        return self._resultado


class CalculadoraPromedio:
    """Clase para calcular el promedio de una lista de valores."""

    def __init__(self, valores):
        self.valores = valores

    def calcular_promedio(self):
        """Calcula y devuelve el promedio de los valores."""
        return sum(self.valores) / len(self.valores) if self.valores else 0


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.resultado}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.resultado}")

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedio = calculadora_promedio.calcular_promedio()
    print(f"El promedio de los números es: {promedio}")
