import ConectaBBDD

def insertar():
    conexion = ConectaBBDD.conectaBBDD('empresa')
    cursor = conexion.cursor()
    nombre_departamento= input("Que nombre de departamento quiere insertar: ")
    insertarempresa = f'''Insert into departamento (nombredep) values ('{nombre_departamento}');'''    
    cursor.execute(insertarempresa)
    conexion.commit()
    cursor.close()
    conexion.close()

def listarvalores():
    conexion = ConectaBBDD.conectaBBDD('empresa')
    cursor = conexion.cursor()
    ver_registros_departamento='''Select * from departamento;'''
    cursor.execute(ver_registros_departamento)
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)
    cursor.close
    conexion.close

def modificarregistro():
    conexion = ConectaBBDD.conectaBBDD('empresa')
    cursor = conexion.cursor()
    nombredepacambiar= input("que numdep quiere cambiar el nombre: ")
    nombrenuevo=input("Que nombre va a ser el nuevo: ")
    actualizar = f'''UPDATE departamento SET nombredep = '{nombrenuevo}' WHERE numdep = {nombredepacambiar};'''
    cursor.execute(actualizar)
    conexion.commit()
    cursor.close()
    conexion.close()
    listarvalores()


def Eliminarregistro():
    conexion = ConectaBBDD.conectaBBDD('empresa')
    cursor = conexion.cursor()
    numdepeliminar= input("que numdep quiere borrar: ")
    eliminar = f'''DELETE FROM departamento WHERE numdep = {numdepeliminar};'''
    cursor.execute(eliminar)
    cursor.close()
    conexion.close()
    listarvalores()


def menu():
    opcion=0
    print("Menú BBDD empresa")
    print("1. Insertar registro")
    print("2. Listar registros")
    print("3. Modificar registro")
    print("4. Eliminar registro")
    print("5. Salir")
    while opcion != 5:
        opcion = input("Elige una opción: ")
        if opcion == "1":
            insertar()
        elif opcion == "2":
            listarvalores()
        elif opcion == "3":
            modificarregistro()
        elif opcion == "4":
            Eliminarregistro()
        elif opcion == "5":
            print("adiós")
        else:
            print("Opción no válida, por favor elige una opción del menú")