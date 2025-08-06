from fin_utils import comparar_lineal_vs_compuesto

def main():
    monto = 10000.0
    tasa = 8.0      # % anual
    dias = 20

    lin, comp, diff = comparar_lineal_vs_compuesto(monto, tasa, dias)
    print(f"Interés simple   : {lin:.4f}")
    print(f"Interés compuesto: {comp:.4f}")
    print(f"Diferencia       : {diff:.4f}")

if __name__ == "__main__":
    main()