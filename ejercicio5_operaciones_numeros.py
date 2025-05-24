import math

def promedio(numeros):
    return sum(numeros) / len(numeros)

def promedio_multiplicativo(numeros):
    producto = 1
    for n in numeros:
        producto *= n
    return producto ** (1/len(numeros))

def potencia_mayor_menor(numeros):
    mayor = max(numeros)
    menor = min(numeros)
    return mayor ** menor

def raiz_cubica_menor(numeros):
    menor = min(numeros)
    return menor ** (1/3)

# Entrada de datos
numeros = []
for i in range(5):
    n = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(n)

# Resultados
print("Promedio:", promedio(numeros))
print("Promedio multiplicativo:", promedio_multiplicativo(numeros))
print("Potencia del mayor al menor:", potencia_mayor_menor(numeros))
print("Raíz cúbica del menor número:", raiz_cubica_menor(numeros))
