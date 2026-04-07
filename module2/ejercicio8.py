def pedir_numeros():
    numero1 = int(input("Dime el 1er número: "))
    numero2 = int(input("Dime el 2o número: "))
    return numero1, numero2

def menu():
    opcion = input("Elige una opción:\n1 - Sumar\n2 - Restar\n3 - Salir\n")
    if opcion == "1":
        sumar()
    elif opcion == "2":
        restar()
    elif opcion == "3":
        print("Hasta luego maricarmen")

    else:
        print("Sabes leer?")

def sumar():
    num1, num2 = pedir_numeros()
    suma = num1 + num2
    print(f"El resultado es: {suma}")

def restar():
    num1, num2 = pedir_numeros()
    resta = num1 - num2
    print(f"El resultado es: {resta}")

menu()