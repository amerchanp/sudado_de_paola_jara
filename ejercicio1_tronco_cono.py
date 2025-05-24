import math

# Función para calcular volumen
def calcular_volumen(r1, r2, h):
    volumen = (1/3) * math.pi * h * (r1**2 + r1*r2 + r2**2)
    return volumen

# Función para calcular área superficial
def calcular_area_superficial(r1, r2, h):
    l = math.sqrt((r1 - r2)**2 + h**2)  # generatriz
    area = math.pi * (r1 + r2) * l + math.pi * r1**2 + math.pi * r2**2
    return area

# Función para pedir valores al usuario
def ingresar_valores():
    r1 = float(input("Ingrese el valor de r1: "))
    r2 = float(input("Ingrese el valor de r2: "))
    h = float(input("Ingrese el valor de h: "))
    return r1, r2, h

# Programa principal
r1, r2, h = ingresar_valores()

volumen = calcular_volumen(r1, r2, h)
area = calcular_area_superficial(r1, r2, h)

print(f"\nVolumen del tronco de cono: {volumen:.2f} unidades cúbicas")
print(f"Área superficial del tronco de cono: {area:.2f} unidades cuadradas")
