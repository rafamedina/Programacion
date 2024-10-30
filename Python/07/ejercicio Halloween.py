import random as R
from functools import reduce
'''
¡Bienvenido a la caza de monstruos de Halloween!
Un vampiro ha aparecido con dificultad 3.


Tienes 3 intentos restantes.
Elige un objeto para intentar capturar al vampiro: estaca, poción mágica, hechizo
Escribe el nombre del objeto: estaca
Fallaste al intentar capturar al vampiro con un/a estaca.


Tienes 2 intentos restantes.
Elige un objeto para intentar capturar al vampiro: estaca, poción mágica, hechizo
Escribe el nombre del objeto: hechizo
Fallaste al intentar capturar al vampiro con un/a hechizo.


Tienes 1 intentos restantes.
Elige un objeto para intentar capturar al vampiro: estaca, poción mágica, hechizo
Escribe el nombre del objeto: poción mágica
¡Has capturado al vampiro con un/a poción mágica!
'''

monstruos = {
    1 : "vampiro",
    2 : "zombie",
    5 : "dragon",
    4 : "sucubo",
    3 : "payaso",
}

objetos = (
    "estaca",
    "poción mágica",
    "hechizo",
    "espada",
    "escudo",
    "armadura",
    "anillo mágico",
    "varita",
    "piedra preciosa",
    "libro de hechizos"
)

intentos = 3
print("¡Bienvenido a la caza de monstruos de Halloween!")
def Invocar_monstruo(lista):
    bicho=R.randint(1,5)
    return bicho

objetos_sin_comillas = ", ".join(objetos)
while True:
    bicho2=(Invocar_monstruo(monstruos))

    dificultad=R.randint(1,5)
    print((f"te has encontrado con {monstruos[bicho2]} con un nivel de diciultad {dificultad}"))

    print(f"Tienes {intentos} intentos restantes: ")
    print(f"Elige un objeto para intentar capturar al {monstruos[bicho2]}: {objetos_sin_comillas}")
    opcion_objeto=input("Escribe el nombre del objeto: ")
    if dificultad 