"""
fin_utils.py - utilidades financieras básicas para microempresas.
"""

DAYS_PER_YEAR = 365

def interes_simple(monto: float, tasa_anual_pct: float, dias: int) -> float:
    if monto <= 0 or tasa_anual_pct < 0 or dias <= 0:
        raise ValueError("monto>0, tasa>=0 y dias>0.")
    return monto * (tasa_anual_pct / 100) * (dias / DAYS_PER_YEAR)

def tasa_diaria(tasa_anual_pct: float) -> float:
    if tasa_anual_pct < 0:
        raise ValueError("La tasa no puede ser negativa.")
    return (1 + tasa_anual_pct / 100) ** (1 / DAYS_PER_YEAR) - 1

def interes_compuesto_diario(monto: float, tasa_anual_pct: float, dias: int) -> float:
    if monto <= 0 or dias <= 0:
        raise ValueError("monto>0 y dias>0.")
    return monto * ((1 + tasa_diaria(tasa_anual_pct)) ** dias - 1)

def comparar_lineal_vs_compuesto(monto: float, tasa_anual_pct: float, dias: int):
    lin = interes_simple(monto, tasa_anual_pct, dias)
    comp = interes_compuesto_diario(monto, tasa_anual_pct, dias)
    return lin, comp, abs(lin - comp)