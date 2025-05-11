def ejercicio_01():
    for x in range(101):
        print(x)

def ejercicio_02():
    numero = int(input("Ingrese un numero entero: "))
    cont = 0
    while numero != 0:
        cont += 1
        numero //= 10
    print(cont)

def ejercicio_03():
    numero_1 = int(input("Ingrese el primer numero: "))
    numero_2 = int(input("Ingrese el segundo numero: "))
    sum = 0

    for x in range(numero_1 + 1, numero_2):
        sum += x

    print(f"Suma: {sum}")

def ejercicio_04():
    numero = int(input("Ingrese un numero: "))
    sum = 0

    while numero != 0:
        sum += numero
        numero = int(input("Ingrese un numero: "))

    print(f"Resultado de la suma: {sum}")

def ejercicio_05():
    from random import randint
    num_aleatorio = randint(0, 9)

    print(num_aleatorio)

    num_ingresado = int(input("Ingrese un numero entre el 1 y el 10: "))
    while num_ingresado != num_aleatorio:
        num_ingresado = int(input("Numero incorrecto. Ingrese otro numero: "))
    print("Enorme!")

def ejercicio_06():
    for x in range(100, 0, -2):
        print(x)

def ejercicio_07():
    num_ingresado = int(input("Ingrese un numero entero positivo: "))
    if(num_ingresado > 0):
        sum = 0
        for x in range(0, num_ingresado):
            sum += x
        print(f"La suma final da como resultado: {sum}")
    else:
        print("Numero ingrsado no valido")

def ejercicio_08():
    cont_pares = 0
    cont_impares = 0
    cont_pos = 0
    cont_neg = 0
    for x in range(100):

        num_ingresado = int(input("Ingrese un numero: "))

        if num_ingresado >= 0:
            cont_pos += 1
        else:
            cont_neg += 1

        if num_ingresado % 2 == 0:
            cont_pares += 1
        else:
            cont_impares += 1

    print(f"Cantidad de numeros positivos ingresados: {cont_pos}")
    print(f"Cantidad de numeros negativos ingresados: {cont_neg}")
    print(f"Cantidad de numeros pares ingresados: {cont_pares}")
    print(f"Cantidad de numeros impares ingresados: {cont_impares}")

def ejercicio_09():
    sum = 0
    cont = 0
    for x in range(100):
        sum += int(input("Ingrese un numero: "))
        cont += 1
    print(f"La media de los valores ingresados es: {sum / cont}")

def ejercicio_10():
    num_ingresado = input("Ingrese un numero: ")
    resultado = ""
    for x in range(len(num_ingresado), 0, -1):
        resultado += num_ingresado[x-1]
    print(f"Numero invertido: {resultado}")