nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
if edad < 12:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
else:
    print("Eres un adulto.")