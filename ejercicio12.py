def pedir_numeros():
    while True:
        try:
            numero1 = int(input("Dime el 1er número: "))
            numero2 = int(input("Dime el 2o número: "))
            return numero1, numero2
        except ValueError:
            print("Eso no es un número. Inténtalo otra vez.")


def operar(num1, num2, operacion):
    if operacion == "+":
        print(f"El resultado es: {num1 + num2}")
    elif operacion == "-":
        print(f"El resultado es: {num1 - num2}")
    elif operacion == "*":
        print(f"El resultado es: {num1 * num2}")
    elif operacion == "/":
        if num2 == 0:
            print("No se puede dividir entre 0")
        else:
            print(f"El resultado es: {num1 / num2}")


def menu():
    return input("\nElige una opción:\n1 - Sumar\n2 - Restar\n3 - Multiplicar\n4 - Dividir\n5 - Salir\n")


def main():
    while True:
        opcion = menu()

        if opcion == "1":
            num1, num2 = pedir_numeros()
            operar(num1, num2, "+")
        elif opcion == "2":
            num1, num2 = pedir_numeros()
            operar(num1, num2, "-")
        elif opcion == "3":
            num1, num2 = pedir_numeros()
            operar(num1, num2, "*")
        elif opcion == "4":
            num1, num2 = pedir_numeros()
            operar(num1, num2, "/")
        elif opcion == "5":
            print("Hasta luego")
            break
        else:
            print("Opción no válida")


main()