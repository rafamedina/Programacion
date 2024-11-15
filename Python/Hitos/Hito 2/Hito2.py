import random  # Importamos la librería random para generar números aleatorios

# Creamos un diccionario para registrar los clientes con su DNI y nombre
listaregistro = {
    "12345678A": "Juan",
    "87654321B": "Ana",
    "11223344C": "Luis",
    "33445566D": "María",
    "99887766E": "Carlos"
}
carritocompra = []  # Lista para guardar los productos que el cliente quiere comprar
seguimientocompra = {}  # Diccionario para seguir los pedidos realizados
listadeproductos = [  # Lista de productos disponibles en la tienda con su precio
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

# Función para registrar o iniciar sesión de un cliente
def registro(lista):
    while True:
        idcliente = input('Ingrese su DNI para el inicio de sesión o registro: ')
        if idcliente in lista:  # Si el DNI ya está registrado
            print(f"Bienvenido de nuevo, {lista[idcliente]}!")
            return idcliente
        else:  # Si el DNI no está registrado
            print('Número no registrado, procedemos con el registro.')
            nombrecliente = input('Introduce tu nombre: ')
            lista[idcliente] = nombrecliente  # Registramos al nuevo cliente
            print(f"Cliente registrado con éxito: {nombrecliente}")
            return idcliente

# Función para mostrar todos los clientes registrados
def visualizarclientes(lista):
    if lista:  # Si hay clientes registrados
        print("Lista de clientes registrados:")
        for dni, nombre in lista.items():
            print(f"DNI: {dni}, Nombre: {nombre}")
    else:
        print("No hay clientes registrados.")

# Función para buscar un cliente por su DNI
def buscarclientes(lista):    
    while True:
        busqueda = input('¿Qué DNI quiere buscar? Ingrese "fin" para salir de la búsqueda: ')
        if busqueda.lower() == 'fin':  # Si el usuario quiere salir
            print("Saliendo de la búsqueda.")
            break
        elif busqueda in lista:  # Si el DNI está en la lista
            print(f'Cliente encontrado: {lista[busqueda]}')
        else:
            print('DNI no encontrado en la lista de clientes.')

# Función para mostrar los productos disponibles
def mostrarproductos():
    print("\nProductos disponibles:")
    for item in listadeproductos:
        print(f"{item['nombre']} - Precio: {item['precio']}€")

# Función para añadir productos al carrito de compras
def añadirproductoacarrito():
    mostrarproductos()  # Mostramos los productos
    while True:
        añadiracarro = input('Selecciona qué quieres añadir al carrito (escribe "fin" para salir): ')
        if añadiracarro.lower() == 'fin':  # Si el usuario quiere salir
            print("Saliendo de la compra.")
            break
        for item in listadeproductos:  # Buscamos el producto en la lista
            if item['nombre'].lower() == añadiracarro.lower():
                carritocompra.append(item)  # Añadimos el producto al carrito
                print(f"{item['nombre']} ha sido añadido al carrito.")
                break
        else:
            print(f"Producto '{añadiracarro}' no encontrado. Inténtalo nuevamente.")

# Función para mostrar el contenido del carrito
def mostrarcarrito():
    if not carritocompra:  # Si el carrito está vacío
        print("El carrito está vacío.")
    else:
        print("\nContenido del carrito:")
        total = sum(item['precio'] for item in carritocompra)  # Calculamos el total
        for item in carritocompra:
            print(f"{item['nombre']} - Precio: {item['precio']}€")
        print(f"Total de la compra: {total}€")

# Función para realizar la compra
def realizar_compra(dni_cliente):
    if not carritocompra:  # Si el carrito está vacío
        print("El carrito está vacío. No se puede realizar la compra.")
        return
    total = sum(item['precio'] for item in carritocompra)  # Calculamos el total de la compra
    print(f"Total a pagar por {dni_cliente}: {total}€")
    confirmacion = input("¿Desea confirmar la compra? (sí/no): ")
    if confirmacion.lower() == 'sí':  # Si el cliente confirma la compra
        seguimientocompra[dni_cliente] = carritocompra.copy()  # Guardamos el pedido
        print("Compra realizada con éxito.")
        carritocompra.clear()  # Limpiamos el carrito después de la compra
    else:
        print("Compra cancelada.")

# Función principal para ejecutar el programa
def main():
    print("Bienvenido a la tienda.")
    dni_cliente = registro(listaregistro)  # Registramos o iniciamos sesión
    while True:
        print("\nOpciones:")
        print("1. Visualizar clientes")
        print("2. Buscar cliente")
        print("3. Añadir producto al carrito")
        print("4. Mostrar carrito")
        print("5. Realizar compra")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            visualizarclientes(listaregistro)  # Mostramos los clientes
        elif opcion == '2':
            buscarclientes(listaregistro)  # Buscamos un cliente
        elif opcion == '3':
            añadirproductoacarrito()  # Añadimos productos al carrito
        elif opcion == '4':
            mostrarcarrito()  # Mostramos el carrito
        elif opcion == '5':
            realizar_compra(dni_cliente)  # Realizamos la compra
        elif opcion == '6':
            print("Gracias por visitar la tienda. ¡Hasta luego!")
            break  # Salimos del programa
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutamos el programa
if __name__ == "__main__":
    main()  # Llamamos a la función principal para iniciar el programa