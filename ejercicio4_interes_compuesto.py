def interes_compuesto(C, i, n):
    return C * (1 + i / 100) ** n

# Entrada de datos
C = float(input("Ingrese el capital del préstamo (C): "))
i = float(input("Ingrese el interés mensual en porcentaje (i): "))
n = int(input("Ingrese el número de meses (n): "))

# Salida
print("Valor final del préstamo:", interes_compuesto(C, i, n))
