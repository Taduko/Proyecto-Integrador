#Inicio del juego
from readchar import readkey, key

nombre = input("Ingrese su nombre: ")
print("Bienvenido al juego", nombre)

#Bucle infinito hasta apretar la tecla UP

while True:
    tecla = readkey()
    if tecla == key.UP:
        print("Has presionado la tecla UP")
        break
    else:
        print("Tecla incorrecta")