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
    for i in range(5):
        num = pedir_numero()
        guardar_numero(num)

def mostrar_numeros():
    print(f"Números introducidos: {lista_numeros}")


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
    mostrar_suma()
    mostrar_cantidad()
    mostrar_media()
    mostrar_pares()
    mostrar_mayores()
    mostrar_max_min()
main()


