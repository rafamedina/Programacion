import random as R

monstruos = {
    1 : "vampiro con dificultad 1",
    2 : "zombie con dificultad 2",
    5 : "dragon con dificultad 5",
    4 : "sucubo con dificultad 4",
    3 : "payaso con dificultad 3",
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
bicho2=(Invocar_monstruo(monstruos))

print(f"te has encontrado con {monstruos[bicho2]}")

print(f"Tienes {intentos} intentos restantes: ")