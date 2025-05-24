# RETO 5
En este caso se desarrollan 7 ejercicios, 5 de ellos en python y 2 de investigación.

## Ejercicio 1
Dado la figura de la imagen, desarrolle:
<div align='center'>
<figure> <img src="https://i.postimg.cc/FRvCmpxx/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el volumen y el área superficial.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

```
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

```

## Ejercicio 2
Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/1t4MrzsL/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

```
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

```

## Ejercicio 3
Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```
def calcular_carne(n, m, k):
    return n * 6 + m * 7 + k * 1

# Entrada de datos
n = int(input("Ingrese el número de gallinas: "))
m = int(input("Ingrese el número de gallos: "))
k = int(input("Ingrese el número de pollitos: "))

# Salida
print("Total de carne (kg):", calcular_carne(n, m, k))

```

## Ejercicio 4
Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

```
def interes_compuesto(C, i, n):
    return C * (1 + i / 100) ** n

# Entrada de datos
C = float(input("Ingrese el capital del préstamo (C): "))
i = float(input("Ingrese el interés mensual en porcentaje (i): "))
n = int(input("Ingrese el número de meses (n): "))

# Salida
print("Valor final del préstamo:", interes_compuesto(C, i, n))

```

## Ejercicio 5
Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

```
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

```

## Ejercicio 6
Consultar qué es y cómo funciona *pip* en python:

pip es una herramienta de línea de comandos que permite instalar, actualizar y desinstalar paquetes de Python desde el Python Package Index (PyPI).

Funciona con comandos como:

    pip install nombre_paquete   # Instala un paquete
    pip uninstall nombre_paquete # Desinstala un paquete
    pip list                     # Muestra los paquetes instalados
    pip show nombre_paquete      # Muestra información de un paquete

pip viene instalado por defecto en las versiones modernas de Python.


## Ejercicio 7
Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos:

Algunos módulos populares de Python que se pueden instalar con pip son:

- numpy → para cálculos numéricos
    pip install numpy
- pandas → para análisis y manejo de datos
    pip install pandas
- matplotlib → para gráficos y visualización
    pip install matplotlib
- requests → para hacer solicitudes HTTP
    pip install requests
- flask → para crear aplicaciones web
    pip install flask

Para instalar cualquiera de estos, abre la terminal y escribe: pip install nombre_del_paquete

### Eso es todo, gracias.
