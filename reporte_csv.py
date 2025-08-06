import csv
from collections import defaultdict

INPUT = "ventas_semana.csv"
OUTPUT = "reporte_semana.csv"

def leer_ventas(path):
    ventas = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                cantidad = int(row["cantidad"])
                precio = float(row["precio_unitario"])
                total_linea = cantidad * precio
                ventas.append({
                    "fecha": row["fecha"],
                    "producto": row["producto"],
                    "cantidad": cantidad,
                    "precio_unitario": precio,
                    "total_linea": total_linea
                })
            except (KeyError, ValueError):
                # Si hay filas corruptas, las saltamos (podrías loguearlas)
                continue
    return ventas

def resumen_ventas(ventas):
    total = sum(v["total_linea"] for v in ventas)
    n_transacciones = len(ventas)
    items_vendidos = sum(v["cantidad"] for v in ventas)
    promedio_ticket = total / n_transacciones if n_transacciones else 0.0

    por_producto = defaultdict(lambda: {"cantidad": 0, "ingreso": 0.0})
    for v in ventas:
        p = v["producto"]
        por_producto[p]["cantidad"] += v["cantidad"]
        por_producto[p]["ingreso"]  += v["total_linea"]

    # Top por ingreso
    top_producto = max(por_producto.items(), key=lambda kv: kv[1]["ingreso"]) if por_producto else None

    return {
        "total_ingresos": total,
        "n_transacciones": n_transacciones,
        "items_vendidos": items_vendidos,
        "promedio_ticket": promedio_ticket,
        "por_producto": por_producto,
        "top_producto": top_producto
    }

def exportar_resumen(resumen, path_out):
    # Exportamos un reporte "tabular" por producto
    with open(path_out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["producto", "cantidad_total", "ingreso_total"])
        for producto, info in resumen["por_producto"].items():
            writer.writerow([producto, info["cantidad"], f"{info['ingreso']:.2f}"])

if __name__ == "__main__":
    ventas = leer_ventas(INPUT)
    r = resumen_ventas(ventas)

    print(f"Total ingresos      : ${r['total_ingresos']:.2f}")
    print(f"Transacciones       : {r['n_transacciones']}")
    print(f"Items vendidos      : {r['items_vendidos']}")
    print(f"Promedio por ticket : ${r['promedio_ticket']:.2f}")

    if r["top_producto"]:
        top_p, info = r["top_producto"]
        print(f"Top producto        : {top_p} (${info['ingreso']:.2f})")

    exportar_resumen(r, OUTPUT)
    print(f"\nReporte por producto exportado a: {OUTPUT}")