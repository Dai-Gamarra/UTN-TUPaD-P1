## TP4 - Estructuras Repetitivas - UTN A Distancia
# Menú interactivo

def ejercicio_1():
    # 1) Imprimir del 0 al 100 en orden creciente
    for numero in range(101):
        print(numero)

def ejercicio_2():
    # 2) Contar cuántos dígitos tiene un número ingresado
    numero = input("Ingrese un número entero: ")
    print(f"El número tiene {len(numero)} dígitos.")

def ejercicio_3():
    # 3) Sumar todos los enteros entre dos valores (excluyéndolos)
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    suma = 0
    for i in range(min(a, b) + 1, max(a, b)):
        suma += i
    print(f"La suma de los números entre {a} y {b} es: {suma}")

def ejercicio_4():
    # 4) Ingresar números hasta que se ingrese 0, acumular la suma
    total = 0
    while True:
        n = int(input("Ingrese un número (0 para terminar): "))
        if n == 0:
            break
        total += n
    print(f"La suma total es: {total}")

def ejercicio_5():
    # 5) Juego de adivinar un número aleatorio entre 0 y 9
    import random
    aleatorio = random.randint(0, 9)
    intentos = 0
    while True:
        guess = int(input("Adivine el número (entre 0 y 9): "))
        intentos += 1
        if guess == aleatorio:
            break
    print(f"¡Correcto! Lo lograste en {intentos} intento(s).")

def ejercicio_6():
    # 6) Imprimir números pares entre 0 y 100 en orden decreciente
    for i in range(100, -1, -1):
        if i % 2 == 0:
            print(i)

def ejercicio_7():
    # 7) Sumar números desde 0 hasta un valor ingresado
    limite = int(input("Ingrese un número entero positivo: "))
    suma = 0
    for i in range(limite + 1):
        suma += i
    print(f"La suma desde 0 hasta {limite} es: {suma}")

def ejercicio_8():
    # 8) Ingresar 100 números y contar pares, impares, positivos y negativos
    cantidad = int(input("¿Cuántos números desea ingresar? (hasta 100): "))
    pares = impares = positivos = negativos = 0
    for i in range(cantidad):
        n = int(input("Ingrese un número: "))
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
        if n >= 0:
            positivos += 1
        else:
            negativos += 1
    print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

def ejercicio_9():
    # 9) Ingresar 100 números y calcular la media
    cantidad = int(input("¿Cuántos números desea ingresar? (hasta 100): "))
    total = 0
    for i in range(cantidad):
        n = int(input("Ingrese un número: "))
        total += n
    media = total / cantidad
    print(f"La media es: {media}")

def ejercicio_10():
    # 10) Invertir los dígitos de un número
    numero = input("Ingrese un número: ")
    invertido = numero[::-1]
    print(f"El número invertido es: {invertido}")

def menu():
    while True:
        print("\nTP 4 - Estructuras Repetitivas - Menú de ejercicios")
        print("1. Números del 0 al 100")
        print("2. Contar dígitos de un número")
        print("3. Sumar entre dos valores (excluidos)")
        print("4. Suma hasta ingresar 0")
        print("5. Adivinar un número (0 a 9)")
        print("6. Pares del 100 al 0")
        print("7. Suma hasta un número")
        print("8. Contar pares, impares, positivos y negativos")
        print("9. Calcular media de N números")
        print("10. Invertir número")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            ejercicio_4()
        elif opcion == "5":
            ejercicio_5()
        elif opcion == "6":
            ejercicio_6()
        elif opcion == "7":
            ejercicio_7()
        elif opcion == "8":
            ejercicio_8()
        elif opcion == "9":
            ejercicio_9()
        elif opcion == "10":
            ejercicio_10()
        elif opcion == "0":
            print("Fin del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()
