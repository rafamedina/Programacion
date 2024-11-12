import random

# Diccionarios para registrar clientes y pedidos
listaregistro = {
    "12345678A": "Juan",
    "87654321B": "Ana",
    "11223344C": "Luis",
    "33445566D": "María",
    "99887766E": "Carlos"
}
carritocompra = []
seguimientocompra = {}
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

def registro(lista):
    while True:
        idcliente = input('Ingrese su DNI para el inicio de sesión o registro: ')
        if idcliente in lista:
            print(f"Bienvenido de nuevo, {lista[idcliente]}!")
            return idcliente
        else:
            print('Número no registrado, procedemos con el registro.')
            nombrecliente = input('Introduce tu nombre: ')
            lista[idcliente] = nombrecliente
            print(f"Cliente registrado con éxito: {nombrecliente}")
            return idcliente

def visualizarclientes(lista):
    # Mostrar lista de todos los clientes registrados
    if lista:
        print("Lista de clientes registrados:")
        for dni, nombre in lista.items():
            print(f"DNI: {dni}, Nombre: {nombre}")
    else:
        print("No hay clientes registrados.")

def buscarclientes(lista):    
    while True:
        busqueda = input('¿Qué DNI quiere buscar? Ingrese "fin" para salir de la búsqueda: ')
        if busqueda.lower() == 'fin':
            print("Saliendo de la búsqueda.")
            break
        elif busqueda in lista:
            print(f'Cliente encontrado: {lista[busqueda]}')
        else:
            print('DNI no encontrado en la lista de clientes.')

def mostrarproductos():
    print("\nProductos disponibles:")
    for item in listadeproductos:
        print(f"{item['nombre']} - Precio: {item['precio']}€")

def añadirproductoacarrito():
    mostrarproductos()  # Mostrar los productos disponibles
    while True:
        añadiracarro = input('Selecciona qué quieres añadir al carrito (escribe "fin" para salir): ')
        if añadiracarro.lower() == 'fin':
            print("Saliendo de la compra.")
            break
        for item in listadeproductos:
            if item['nombre'].lower() == añadiracarro.lower():
                carritocompra.append(item)
                print(f"{item['nombre']} ha sido añadido al carrito.")
                break
        else:
            print(f"Producto '{añadiracarro}' no encontrado. Inténtalo nuevamente.")

def mostrarcarrito():
    if not carritocompra:
        print("El carrito está vacío.")
    else:
        print("\nContenido del carrito:")
        total = sum(item['precio'] for item in carritocompra)
        for item in carritocompra:
            print(f"{item['nombre']} - Precio: {item['precio']}€")
        print(f"Total de la compra: {total}€")

def realizar_compra(dni_cliente):
    if not carritocompra:
        print("El carrito está vacío. No se puede realizar la compra.")
        return
    numero_pedido = random.randint(1000, 9999)
    productos = [item['nombre'] for item in carritocompra]
    total = sum(item['precio'] for item in carritocompra)
    seguimientocompra[numero_pedido] = {
        "cliente_dni": dni_cliente,
        "productos": productos,
        "total": total
    }
    print(f"Pedido realizado con éxito. Número de pedido: {numero_pedido}")
    carritocompra.clear()

def seguimiento_pedido():
    try:
        numero_pedido = int(input("Ingrese el número de pedido para realizar el seguimiento: "))
        if numero_pedido in seguimientocompra:
            pedido = seguimientocompra[numero_pedido]
            dni_cliente = pedido["cliente_dni"]
            nombre_cliente = listaregistro[dni_cliente]
            print(f"\nDetalles del Pedido #{numero_pedido}:")
            print(f"Cliente: {nombre_cliente}, DNI: {dni_cliente}")
            print("Productos comprados:")
            for producto in pedido["productos"]:
                print(f"- {producto}")
            print(f"Total: {pedido['total']}€")
        else:
            print("Pedido no encontrado.")
    except ValueError:
        print("Número de pedido no válido.")

# Función principal para interactuar con el sistema
def menu():
    dni_cliente_actual = 0

    # Requerir inicio de sesión o registro antes de acceder al menú
    while dni_cliente_actual == 0:
        dni_cliente_actual = registro(listaregistro)

    # Mostrar el menú solo si se ha registrado o iniciado sesión
    while True:
        print("\n--- Menú de la tienda ---")
        print("1. Visualizar clientes registrados")
        print("2. Buscar cliente por DNI")
        print("3. Ver productos disponibles")
        print("4. Añadir producto al carrito")
        print("5. Ver carrito de compras")
        print("6. Realizar compra")
        print("7. Seguimiento de pedido")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            visualizarclientes(listaregistro)
        elif opcion == '2':
            buscarclientes(listaregistro)
        elif opcion == '3':
            mostrarproductos()
        elif opcion == '4':
            añadirproductoacarrito()
        elif opcion == '5':
            mostrarcarrito()
        elif opcion == '6':
            realizar_compra(dni_cliente_actual)
        elif opcion == '7':
            seguimiento_pedido()
        elif opcion == '8':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Llamada a la función principal

menu()


