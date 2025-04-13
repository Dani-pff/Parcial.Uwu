# Menú para los clientes
def menu_clientes():
    print("\n--- Menú de Clientes ---")
    print("1. Registrar cliente")
    print("2. Consultar cliente")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    print("0. Volver al menú principal")
    return int(input("Selecciona una opción válida: "))

def registrar_cliente():
    nombre = input("Nombre del cliente: ")
    id = input("Identificación: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    return (nombre, id, telefono, direccion)

def buscar_cliente(id, clientes):
    for cliente in clientes:
        if cliente[1] == id:
            return cliente
    return None

def actualizar_cliente(id, clientes):
    for i, cliente in enumerate(clientes):
        if cliente[1] == id:
            print("Ingrese los nuevos datos:")
            clientes[i] = registrar_cliente()
            print("Cliente actualizado.")
            return
    print("Cliente no encontrado.")

def eliminar_cliente(id, clientes, bienes):
    for cliente in clientes:
        if cliente[1] == id:
            clientes.remove(cliente)
            if id in bienes:
                del bienes[id]
            print("Cliente eliminado.")
            return
    print("Cliente no encontrado.")


# Menú para los bienes
def menu_bienes():
    print("\n--- Menú de Bienes ---")
    print("1. Registrar bien")
    print("2. Modificar bien")
    print("3. Listar bienes")
    print("4. Eliminar bien")
    print("0. Volver al menú principal")
    return int(input("Selecciona una opción válida: "))

def registrar_bien(id, bienes):
    if id not in bienes:
        bienes[id] = []
    nombre = input("Nombre del artículo: ")
    cantidad = int(input("Cantidad: "))
    disponible = input("¿Está disponible? (s/n): ").lower() == 's'
    bien = {"nombre": nombre, "cantidad": cantidad, "disponible": disponible}
    bienes[id].append(bien)
    print("Bien registrado correctamente.")

def modificar_bien(id, bienes):
    if id in bienes:
        for i, bien in enumerate(bienes[id]):
            print(f"{i+1}. {bien}")
        index = int(input("Seleccione el número del bien a modificar: ")) - 1
        if 0 <= index < len(bienes[id]):
            nombre = input("Nuevo nombre del artículo: ")
            cantidad = int(input("Nueva cantidad: "))
            disponible = input("¿Está disponible? (s/n): ").lower() == 's'
            bienes[id][index] = {"nombre": nombre, "cantidad": cantidad, "disponible": disponible}
            print("Bien modificado.")
        else:
            print("Índice no válido.")
    else:
        print("El cliente no tiene bienes registrados.")

def listar_bienes(id, bienes):
    if id in bienes:
        filtro = input("¿Listar solo disponibles? (s/n): ").lower()
        for bien in bienes[id]:
            if filtro == 's' and not bien["disponible"]:
                continue
            print(bien)
    else:
        print("El cliente no tiene bienes registrados.")

def eliminar_bien(id, bienes):
    if id in bienes:
        for i, bien in enumerate(bienes[id]):
            print(f"{i+1}. {bien}")
        index = int(input("Seleccione el número del bien a eliminar: ")) - 1
        if 0 <= index < len(bienes[id]):
            del bienes[id][index]
            print("Bien eliminado.")
        else:
            print("Índice no válido.")
    else:
        print("El cliente no tiene bienes registrados.")


# Zona de código principal
clientes = []  # Lista de tuplas
bienes = {}    # Diccionario: clave = id del cliente, valor = lista de bienes

while True:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Gestión de clientes")
    print("2. Gestión de bienes")
    print("0. Salir del sistema")
    opcion = int(input("Selecciona una opción válida: "))
    
    match opcion:
        case 1:
            while True:
                opc = menu_clientes()
                match opc:
                    case 1:
                        cliente = registrar_cliente()
                        clientes.append(cliente)
                        print("Cliente registrado.")
                    case 2:
                        id = input("Ingrese identificación del cliente: ")
                        cliente = buscar_cliente(id, clientes)
                        print(cliente if cliente else "Cliente no encontrado.")
                    case 3:
                        id = input("Identificación del cliente a actualizar: ")
                        actualizar_cliente(id, clientes)
                    case 4:
                        id = input("Identificación del cliente a eliminar: ")
                        eliminar_cliente(id, clientes, bienes)
                    case 0:
                        break
                    case _:
                        print("Opción no válida.")
        case 2:
            while True:
                opc = menu_bienes()
                match opc:
                    case 1:
                        id = input("ID del cliente al que agregar bien: ")
                        if buscar_cliente(id, clientes):
                            registrar_bien(id, bienes)
                        else:
                            print("Cliente no encontrado.")
                    case 2:
                        id = input("ID del cliente cuyos bienes desea modificar: ")
                        modificar_bien(id, bienes)
                    case 3:
                        id = input("ID del cliente para listar bienes: ")
                        listar_bienes(id, bienes)
                    case 4:
                        id = input("ID del cliente para eliminar un bien: ")
                        eliminar_bien(id, bienes)
                    case 0:
                        break
                    case _:
                        print("Opción no válida.")
        case 0:
            print("Gracias por usar el sistema.")
            break
        case _:
            print("Opción inválida.")
