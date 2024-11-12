import random
listaregistro={}
listadeproductos = [
    {"nombre": "manzana", "precio": 25},
    {"nombre": "pera", "precio": 20},
    {"nombre": "jamon", "precio": 300},
    {"nombre": "cochino", "precio": 250},
    {"nombre": "mermelada", "precio": 15},
    {"nombre": "montadito del solarino", "precio": 2},
    {"nombre": "panini", "precio": 3},
    {"nombre": "leche", "precio": 2},
    {"nombre": "juguete", "precio": 45.00},
    {"nombre": "movil", "precio": 800}
]

carritocompra=[]
seguimientocompra={}

def registro(lista):
    while True:
        idcliente = input('Ingrese su DNI para el inicio de sesión: ')
        if idcliente in lista:
            
            return True
        else:
            print('número no registrado, procedemos con el registro:')
            registrocliente = input('Indique su DNI para efectuar el registro: ')
            nombrecliente = input('Introduce tu nombre: ')
            lista[registrocliente]=nombrecliente
            for registrocliente, nombrecliente in lista.items():
                print(f'{registrocliente}:{nombrecliente}')


def visualizarclientes(lista):
    # Convertir el diccionario en una lista de strings de forma "DNI: Nombre"
    lista_bonita = ", ".join([f"{idcliente}: {nombre}" for idcliente, nombre in lista.items()])
    print(f'Esta es su lista actual de usuarios:\n{lista_bonita}')


def buscarclientes(lista):    
    # Bucle de búsqueda con opción de salida
    while True:
        busqueda = input('¿Qué DNI quiere buscar? Ingrese fin para salir de la búsqueda: ')
        if busqueda.lower() == 'fin':
            print("Saliendo de la búsqueda.")
            break  # Termina el bucle si el usuario ingresa "0"
        elif busqueda in lista:
            print(f'Cliente encontrado: {lista[busqueda]}')
        else:
            print('DNI no encontrado en la lista de clientes.')

def mostrarproductos():
    for item in listadeproductos:
        print(f"{item['nombre']} - Precio: {item['precio']}€")


def añadirproductoacarrito():
    mostrarproductos()  # Mostrar los productos disponibles
    while True:
        # Solicitar al usuario que seleccione un producto
        añadiracarro = input('Selecciona qué quieres añadir al carrito (escribe "fin" para salir): ')
        if añadiracarro.lower() == 'fin':
            print("Saliendo de la compra.")
            break
        
        # Buscar el producto seleccionado
        for item in listadeproductos:
            if item['nombre'].lower() == añadiracarro.lower():
                # Añadir el producto al carrito
                carritocompra.append(item)
                print(f"{item['nombre']} ha sido añadido al carrito.")
                break
        else:
            # Si no se encontró el producto
            print(f"Producto '{añadiracarro}' no encontrado. Inténtalo nuevamente.")


    
def mostrarcarrito():
    if not carritocompra:
        print("El carrito está vacío.")
    else:
        print("\nContenido del carrito:")
        total = 0
        for item in carritocompra:
            print(f"{item['nombre']} - Precio: {item['precio']}€")
            total += item['precio']
        print(f"Total de la compra: {total}€")

añadirproductoacarrito()