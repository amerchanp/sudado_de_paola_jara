import math

def calcular_area(a, b, r):
    area_rect = a * b
    area_ruedas = 2 * math.pi * r**2
    return area_rect + area_ruedas

def calcular_perimetro(a, b, r):
    perimetro_rect = 2 * (a + b)
    perimetro_ruedas = 2 * (2 * math.pi * r)
    return perimetro_rect + perimetro_ruedas

# Entrada de datos
r = float(input("Ingrese el radio de las ruedas (r): "))
a = float(input("Ingrese la altura del rectángulo (a): "))
b = float(input("Ingrese la base del rectángulo (b): "))

# Salida
print("Área total:", calcular_area(a, b, r))
print("Perímetro total:", calcular_perimetro(a, b, r))
