def calcular_carne(n, m, k):
    return n * 6 + m * 7 + k * 1

# Entrada de datos
n = int(input("Ingrese el número de gallinas: "))
m = int(input("Ingrese el número de gallos: "))
k = int(input("Ingrese el número de pollitos: "))

# Salida
print("Total de carne (kg):", calcular_carne(n, m, k))
