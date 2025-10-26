articulos = []
usuarios = []

def buscar_por_id(lista, id_buscar):
    for item in lista:
        if item["id"] == id_buscar:
            return item
    return None2


def generar_id(articulos):
    if len(articulos) == 0:
        return 1
    else:
        return articulos[-1]["id"] + 1

def crear_articulo(articulos):
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    nuevo = {"id": generar_id(articulos), "nombre": nombre, "precio": precio, "stock": stock, "activo": True}
    articulos.append(nuevo)
    print("Artículo creado.")

def listar_articulos(articulos):
    if len(articulos) == 0:
        print("No hay artículos.")
    else:
        for a in articulos:
            print(a)
        print()

def buscar_articulo_por_id(articulos):
    id_buscar = int(input("ID del artículo: "))
    for a in articulos:
        if a["id"] == id_buscar:
            print(a)
            return a
    print("No encontrado.")
    return None

def actualizar_articulo(articulos):
    a = buscar_articulo_por_id(articulos)
    if a != None:
        nuevo_nombre = input("Nuevo nombre: ")
        if nuevo_nombre != "":
            a["nombre"] = nuevo_nombre
        nuevo_precio = input("Nuevo precio: ")
        if nuevo_precio != "":
            a["precio"] = float(nuevo_precio)
        nuevo_stock = input("Nuevo stock: ")
        if nuevo_stock != "":
            a["stock"] = int(nuevo_stock)
        print("Artículo actualizado.")

def eliminar_articulo(articulos):
    a = buscar_articulo_por_id(articulos)
    if a != None:
        articulos.remove(a)
        print("Artículo eliminado.")

def alternar_activo(articulos):
    a = buscar_articulo_por_id(articulos)
    if a != None:
        a["activo"] = not a["activo"]
        print("Estado cambiado.")

def menu_articulos():
    opcion = ""
    while opcion != "7":
        print("Menu Articulos")
        print("1. Crear artículo")
        print("2. Listar artículos")
        print("3. Buscar por ID")
        print("4. Actualizar artículo")
        print("5. Eliminar artículo")
        print("6. Activar/Inactivar artículo")
        print("7. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            crear_articulo(articulos)
        elif opcion == "2":
            listar_articulos(articulos)
        elif opcion == "3":
            buscar_articulo_por_id(articulos)
        elif opcion == "4":
            actualizar_articulo(articulos)
        elif opcion == "5":
            eliminar_articulo(articulos)
        elif opcion == "6":
            alternar_activo(articulos)
        elif opcion == "7":
            print("Saliendo")

# Menu Usuarios Entrega 2 

def crear_usuario():
    nombre = input("Nombre del usuario: ")
    email = input("Email: ")
    usuario = {"id": generar_id(usuarios), "nombre": nombre, "email": email, "activo": True}
    usuarios.append(usuario)
    print("Usuario creado.")

def listar_usuarios():
    if not usuarios:
        print("No hay usuarios.")
    else:
        for u in usuarios:
            print(u)
        print()

def actualizar_usuario():
    id_buscado = int(input("ID del usuario: "))
    usuario = buscar_por_id(usuarios, id_buscado)
    if usuario:
        nuevo_nombre = input("Nuevo nombre: ")
        if nuevo_nombre:
            usuario["nombre"] = nuevo_nombre
        nuevo_email = input("Nuevo email: ")
        if nuevo_email:
            usuario["email"] = nuevo_email
        print("Usuario actualizado.\n")
    else:
        print("Usuario no encontrado.\n")

def eliminar_usuario():
    id_buscado = int(input("ID del usuario: "))
    usuario = buscar_por_id(usuarios, id_buscado)
    if usuario:
        usuarios.remove(usuario)
        print("Usuario eliminado.")
    else:
        print("Usuario no encontrado.")

def alternar_activo_usuario():
    id_buscado = int(input("ID del usuario: "))
    usuario = buscar_por_id(usuarios, id_buscado)
    if usuario:
        usuario["activo"] = not usuario["activo"]
        print("Estado cambiado.")
    else:
        print("Usuario no encontrado.")

def menu_usuarios():
    opcion = ""
    while opcion != "7":
        print("Menu Usuarios")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Buscar por ID")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Activar/Inactivar usuario")
        print("7. Volver")

        opcion = input("Opción: ")
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            id_buscado = int(input("ID: "))
            usuario = buscar_por_id(usuarios, id_buscado)
            print(usuario or "No encontrado.")
        elif opcion == "4":
            actualizar_usuario()
        elif opcion == "5":
            eliminar_usuario()
        elif opcion == "6":
            alternar_activo_usuario()
        elif opcion == "7":
            print()
        else:
            print("Opción no válida.")

def menu_principal():
    opcion = ""
    while opcion != "3":
        print("Mini Tienda Online")
        print("1. Menú Artículos")
        print("2. Menú Usuarios")
        print("3. Salir")

        opcion = input("Opción: ")
        if opcion == "1":
            menu_articulos()
        elif opcion == "2":
            menu_usuarios()
        elif opcion == "3":
            print("Saliendo")
        else:
            print("Opción no válida.")

menu_principal()
