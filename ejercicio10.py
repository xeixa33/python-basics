def pedir_numeros():
    while True:
        try:
            numero1 = int(input("Dime el 1er número: "))
            numero2 = int(input("Dime el 2o número: "))
            return numero1, numero2
        except ValueError:
            print("Eso no es un número. Inténtalo otra vez.")

def menu():
    return input("\nElige una opción:\n1 - Sumar\n2 - Restar\n3 - Salir\n")
def sumar():
    num1, num2 = pedir_numeros()
    print(f"El resultado es: {num1 + num2}")

def restar():
    num1, num2 = pedir_numeros()
    print(f"El resultado es: {num1 - num2}")

def main():
    while True:
        opcion = menu()

        if opcion == "1":
            sumar()
        elif opcion == "2":
            restar()
        elif opcion == "3":
            print("Hasta luego")
            break
        else:
            print("Opción no válida")

main()
