lista_numeros = []


def pedir_numero():
    while True:
        try:
            numero = int(input("Escríbeme un número: "))
            return numero
        except ValueError:
            print("Introduce un número válido")


def guardar_numero(numero):
    lista_numeros.append(numero)


def registrar_numero():
    for _ in range(5):
        num = pedir_numero()
        guardar_numero(num)


def mostrar_numeros():
    print(f"Números introducidos: {sorted(lista_numeros)}")  # Mostramos la lista ordenada


def mostrar_duplicados():
    duplicados = []  # Guardamos los números repetidos

    for num in set(lista_numeros):  # set() elimina repetidos
        if lista_numeros.count(num) > 1:
            duplicados.append(num)

    if len(duplicados) > 0:
        print("Estos son los números duplicados:")
        for num in duplicados:
            print(f"- {num}")
    else:
        print("No hay números duplicados")


def contar_repeticiones():
    for num in set(lista_numeros):
        veces = lista_numeros.count(num)
        if veces > 1:  # Ajustamos singular/plural
            print(f"{num} aparece: {veces} veces")
        else:
            print(f"{num} aparece: {veces} vez")


def mostrar_suma():
    print(f"Suma total: {sum(lista_numeros)}")


def mostrar_cantidad():
    print(f"Cantidad de números: {len(lista_numeros)}")


def mostrar_media():
    if len(lista_numeros) > 0:
        print(f"Media: {sum(lista_numeros) / len(lista_numeros)}")


def mostrar_pares():
    print("Números pares:")
    for num in lista_numeros:
        if num % 2 == 0:
            print(f"- {num}")


def mostrar_mayores():
    while True:
        try:
            limite = int(input("Número límite: "))
            break
        except ValueError:
            print("Introduce un número válido")

    for num in lista_numeros:
        if num > limite:
            print(f"{num} es mayor que {limite}")


def mostrar_max_min():
    if len(lista_numeros) > 0:
        print(f"El número máximo es: {max(lista_numeros)}")
        print(f"El número mínimo es: {min(lista_numeros)}")


def main():
    registrar_numero()
    mostrar_numeros()
    mostrar_duplicados()
    contar_repeticiones()
    mostrar_suma()
    mostrar_cantidad()
    mostrar_media()
    mostrar_pares()
    mostrar_mayores()
    mostrar_max_min()


main()