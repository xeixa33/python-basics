def pedir_numero():
    while True:
        try:
            numero = int(input("Escríbeme un número: "))
            return numero
        except ValueError:
            print("Introduce un número válido")


def guardar_numero(lista_numeros,numero):
    lista_numeros.append(numero)
    return lista_numeros


def registrar_numero():
    lista_numeros = []
    for _ in range(10):
        num = pedir_numero()
        guardar_numero(lista_numeros,num)
    return lista_numeros


def mostrar_numeros(lista_numeros):
    print(f"Números introducidos: {sorted(lista_numeros)}")  # Mostramos la lista ordenada


def mostrar_duplicados(lista_numeros):
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


def contar_repeticiones(lista_numeros):
    for num in set(lista_numeros):
        veces = lista_numeros.count(num)
        if veces > 1:  # Ajustamos singular/plural
            print(f"{num} aparece: {veces} veces")
        else:
            print(f"{num} aparece: {veces} vez")


def mostrar_suma(lista_numeros):
    print(f"Suma total: {sum(lista_numeros)}")


def mostrar_cantidad(lista_numeros):
    print(f"Cantidad de números: {len(lista_numeros)}")


def mostrar_media(lista_numeros):
    if len(lista_numeros) > 0:
        print(f"Media: {sum(lista_numeros) / len(lista_numeros)}")


def mostrar_pares(lista_numeros):
    print("Números pares:")
    for num in lista_numeros:
        if num % 2 == 0:
            print(f"- {num}")


def mostrar_mayores(lista_numeros):
    while True:
        try:
            limite = int(input("Número límite: "))
            break
        except ValueError:
            print("Introduce un número válido")

    for num in set(lista_numeros): # Añadimos set, para no repetir numeros
        if num > limite:
            print(f"{num} es mayor que {limite}")


def mostrar_max_min(lista_numeros):
    if len(lista_numeros) > 0:
        print(f"El número máximo es: {max(lista_numeros)}")
        print(f"El número mínimo es: {min(lista_numeros)}")


def main():
    lista_numeros = registrar_numero()
    mostrar_numeros(lista_numeros)
    mostrar_duplicados(lista_numeros)
    contar_repeticiones(lista_numeros)
    mostrar_suma(lista_numeros)
    mostrar_cantidad(lista_numeros)
    mostrar_media(lista_numeros)
    mostrar_pares(lista_numeros)
    mostrar_mayores(lista_numeros)
    mostrar_max_min(lista_numeros)


main()