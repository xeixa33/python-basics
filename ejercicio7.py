opcion = input("Elige una opción:\n1 - Sumar\n2 - Restar\n3 - Salir\n")
if opcion == 1:
    num1 = int(input("Dime el 1er número: "))
    num2 = int(input("Dime el 2o número: "))
    suma = num1 + num2
    print(f"El resultado es: {suma}")

elif opcion == 2:
    num1 = int(input("Dime el 1er número: "))
    num2 = int(input("Dime el 2o número: "))
    resta = num1 - num2
    print(f"El resultado es: {resta}")

elif opcion == 3:
    print("Hasta luego maricarmen")

else:
    print("Sabes leer?")