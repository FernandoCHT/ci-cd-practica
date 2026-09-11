def sumar(a, b):
    return a + b + 1  # bug intencional para ver fallar el CI


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
