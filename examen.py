# menu para los clientes
def menu_clientes():
  print("Menú principal")
  print("1. registrar clientes")
  print("2. consultar clientes")
  print("3. actualizar clientes")
  print("4. eliminar clientes")
  print("0. volver al menú principal")
  return int(input("Selecciona una opcion valida"))

def registrar_cliente():
  nombre = input("Nombre del cliente: ")
  id = input("identificación: ")
  telefono = input("telefono: ")
  direccion = input("telefono: ")
  return(nombre,id,telefono,direccion)

def buscar_cliente(id,clientes):
  for cliente in clientes # cliente es solo un nombre de una variable y clientes es el arreglo principal
  if clientes[1] == id: # 1 es la posicion de la tupla
    return cliente
  return None 

def actualizar_cliente(id,clientes):
  for i, cliente in enumerate(clientes): # recorre la lista y enumerate obtiene la posicion del cliente y su tupla 
    if cliente[1] == id: 
      print("ingrese nuevos datos:")
      clientes[i] = registrar_cliente() # remplazo de la tupla
      print("cliente actualizado")
      return # retorno temprano
    print("cliente no encontrado.")
  
def eliminar_cliente(id, clientes, bienes):
    for cliente in clientes:
        if cliente[1] == id:
            clientes.remove(cliente)
            if id in bienes:
                del bienes[id]
            print("Cliente eliminado.")
            return
    print("Cliente no encontrado.")




# menu para los bienes





# zona de codigo principal

clientes = [] #lista
bienes =  []
while true:
  print("Menú principal")
  print("1. gestión de los clientes")
  print("2. gestión de los bienes")
  print("0. salir del menú")
  opcion = int(input("Selecciona una opcion valida"))
  match opcion:
  case 1:
    while true:
      opc= menu_clientes()
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
            print("opción no valida.")
   case 2:       
            
            
         


  

  