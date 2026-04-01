edad = int(input("¿Cuántos años tienes? "))

if edad < 0:
    print("¿Me estás vacilando?")
elif edad < 18:
    print("Aún te quedan muchas cosas por vivir y aprender")
elif edad < 33:
    print("Estás en la flor de la vida, aprovecha cada momento y disfruta")
else:
    print("Si estuviésemos en Lumière, ya habrías fallecido...\nPor suerte para ti no es el caso ;)")
