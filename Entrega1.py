articulos = []

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
            print("Saliendo del programa...")
        else:
            print("Opción no válida.")

menu_articulos()