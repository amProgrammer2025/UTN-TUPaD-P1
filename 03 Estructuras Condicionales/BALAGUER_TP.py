def ejercicio_01():
    edad = int(input("Ingrese su edad: "))

    if edad >= 18:
        print("Es mayor de edad")

def ejercicio_02():
    nota = int(input("Ingrese su nota: "))

    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

def ejercicio_03():
    numero = int(input("Ingrese un numero: "))

    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")

def ejercicio_04():
    edad = int(input("Ingrese su edad: "))

    if edad < 12:
        print("Usted pertenece a la categoria niño")
    elif edad >= 12 and edad < 18:
        print("Usted pertenece a la categoria adolescente")
    elif edad >= 18 and edad < 30:
        print("Usted pertenece a la categoria adulto joven")
    else:
        print("Usted pertenece a la categoria adulto")

def ejercicio_05():
    password = int(input("Ingrese una contraseña entre 8 y 14 caracteres de largo: "))

    if len(password) >= 8 and len(password) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

def ejercicio_06():
    import random
    from statistics import mode, median, mean

    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)

    if media > mediana and mediana> moda:
        print("Existe un sesgo positivo")
    elif media < mediana and mediana < moda:
        print("Existe un sesgo negativo")
    else:
        print("No existe sesgo")

def ejercicio_07():
    palabra = input("Ingrese una palabra o frase: ")

    if palabra[-1].lower() in "aeiou":
        print (f"{palabra}!")
    else:
        print(palabra)

def ejercicio_08():
    nombre = input("Ingrese su nombre: ")
    opcion = int(input("Ingrese una opcion (1, 2 o 3): "))

    if opcion == 1:
        print (nombre.upper())
    elif opcion == 2:
        print (nombre.lower())
    elif opcion == 3:
        print (nombre.title())
    else:
        print("Opcion no valida")

def ejercicio_09():
    magnitud = float(input("Ingrese la magnitud del sismo: "))

    if magnitud < 3:
        print("Muy leve")
    elif magnitud >= 3 and magnitud < 4:
        print("Leve")
    elif magnitud >= 4 and magnitud < 5:
        print("Moderado")
    elif magnitud >= 5 and magnitud < 6:
        print("Fuerte")
    elif magnitud >= 6 and magnitud < 7:
        print("Muy fuerte")
    else:
        print("Extremo")

def ejercicio_10():
    hemisferio = input("Ingrese en que hemisferio se encuentra (N o S): ").upper()
    mes = int(input("Ingrese en que mes del año se encuentra: "))
    dia = int(input("Ingrse en que dia del mes se encuentra: "))

    if mes == 1:
        estacion = "Verano"
    elif mes == 2:
        estacion = "Verano"
    elif mes == 3:
        if dia <= 20:
            estacion = "Verano"
        else:
            estacion = "Otoño"
    elif mes == 4:
        estacion = "Otoño"
    elif mes == 5:
        estacion = "Otoño"
    elif mes == 6:
        if dia <= 20:
            estacion = "Otoño"
        else:
            estacion = "Invierno"
    elif mes == 7:
        estacion = "Invierno"
    elif mes == 8:
        estacion = "Invierno"
    elif mes == 9:
        if dia <= 20:
            estacion = "Invierno"
        else:
            estacion = "Primavera"
    elif mes == 10:
        estacion = "Primavera"
    elif mes == 11:
        estacion = "Primavera"
    elif mes == 12:
        if dia <= 20:
            estacion = "Primavera"
        else:
            estacion = "Verano"

    if hemisferio == 'N':
        if estacion == "Verano":
            estacion = "Invierno"
        elif estacion == "Invierno":
            estacion = "Verano"
        elif estacion == "Primavera":
            estacion = "Otoño"
        elif estacion =="Otoño":
            estacion = "Primavera"

    print(f"El {dia} del mes {mes} es: {estacion}")