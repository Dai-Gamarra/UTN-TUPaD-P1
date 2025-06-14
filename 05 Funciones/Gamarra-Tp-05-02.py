# Ejercicio 1 - Imprimir "Hola Mundo!" usando una función
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

# Ejercicio 2 - Saludar al usuario con su nombre
def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre_ingresado = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_ingresado)
print(saludo)

# Ejercicio 3
# Imprimir información personal del usuario
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# Ejercicio 4
# Calcular área y perímetro de un círculo
def calcular_area_circulo(radio):
    return 3.1416 * radio ** 2
def calcular_perimetro_circulo(radio):
    return 2 * 3.1416 * radio
radio = float(input("Ingrese el radio del círculo: "))
print("Área:", calcular_area_circulo(radio))
print("Perímetro:", calcular_perimetro_circulo(radio))

# Ejercicio 5
# Convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600
segundos = int(input("Ingrese cantidad de segundos: "))
print("Conversión a horas:", round(segundos_a_horas(segundos), 2))

# Ejercicio 6
# Imprimir tabla de multiplicar de un número
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)

# Ejercicio 7
# Operaciones básicas entre dos números
def operaciones_basicas(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else 'Infinito'
a = float(input("Ingrese primer número: "))
b = float(input("Ingrese segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

# Ejercicio 8
# Calcular Índice de Masa Corporal (IMC)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print("IMC:", round(calcular_imc(peso, altura), 2))

# Ejercicio 9
# Convertir grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius = float(input("Ingrese temperatura en Celsius: "))
print("Temperatura en Fahrenheit:", celsius_a_fahrenheit(celsius))

# Ejercicio 10
# Calcular promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3
n1 = float(input("Ingrese primer número: "))
n2 = float(input("Ingrese segundo número: "))
n3 = float(input("Ingrese tercer número: "))
print("Promedio:", round(calcular_promedio(n1, n2, n3), 2))
