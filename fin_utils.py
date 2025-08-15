import math


def interes_simple(principal, tasa, tiempo):
    """Calcula interés simple."""
    if principal <= 0 or tasa < 0 or tiempo < 0:
        raise ValueError("Valores inválidos")
    return principal * (1 + tasa * tiempo)


def tasa_diaria(tasa_anual):
    """Convierte tasa anual a tasa diaria."""
    if tasa_anual < 0:
        raise ValueError("La tasa no puede ser negativa")
    return tasa_anual / 365


def interes_compuesto_diario(principal, tasa, tiempo):
    """Calcula interés compuesto diario."""
    return principal * math.pow(1 + tasa, tiempo)


def comparar_lineal_vs_compuesto(principal, tasa, tiempo):
    """Compara interés simple vs compuesto."""
    simple = interes_simple(principal, tasa, tiempo)
    compuesto = interes_compuesto_diario(principal, tasa, tiempo)
    diferencia = compuesto - simple
    return simple, compuesto, diferencia