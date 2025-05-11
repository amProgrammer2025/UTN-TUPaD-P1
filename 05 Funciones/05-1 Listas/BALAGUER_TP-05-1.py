def ejercicio_01():
    lista = list(range(0, 100, 4))
    print(lista)

def ejercicio_02():
    lista = [0, 1, 2, 231, 4]
    print(lista[len(lista) - 2])

def ejercicio_03():
    lista = []
    lista.append("Palabra_1")
    lista.append("Palabra_2")
    lista.append("Palabra_3")
    print(lista)

def ejercicio_04():
    animales = ["perro", "gato", "conejo", "pez"]
    animales[len(animales) - 2] = "loro"
    animales[len(animales) - 1] = "oso"
    print(animales)

def ejercicio_05():
    # Este codigo encuentra el valor maximo en la lista 'numeros' y lo elimina
    numeros = [8, 15, 3, 22, 7]
    numeros.remove(max(numeros))
    print(numeros)

def ejercicio_06():
    lista = []
    for x in range(10, 30 + 1, 5):
        lista.append(x)
    print(f"{lista[0]} y {lista[1]}")

def ejercicio_07():
    autos = ["sedan", "polo", "suran", "gol"]
    largo_lista = len(autos)

    if largo_lista % 2 != 0:
        autos.remove(autos[largo_lista // 2])
    else:
        autos.remove(autos[largo_lista // 2])
        autos.remove(autos[largo_lista // 2 - 1])
    
    print(autos)

def ejercicio_08():
    dobles = []
    
    for d in range(5, 15 + 1, 5):
        dobles.append(d * 2)

    print(dobles)

def ejercicio_09():
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

    compras[2].append("jugo")
    compras[1][1] = "tallarines"
    compras[0].remove("pan")
    print(compras)

def ejercicio_10():
    lista_anidada = []
    lista_flotante = [25.5, 57.9, 30.6]
    lista_anidada.append(15)
    lista_anidada.append(True)
    lista_anidada.append(lista_flotante)
    lista_anidada.append(False)
    print(lista_anidada)