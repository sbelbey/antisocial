post = {
    "contenido": "",
}

print("Contenido:", post["contenido"])

def eliminar_post():
    post.clear()
    print("El post ha sido eliminado.")

print("Bienvenido a nuestra red social")
contenido = input("Escribe el contenido de tu post: ")

eliminar = input("¿Deseas eliminar este post? (si/no): ")
if eliminar.lower() == "si":
    eliminar_post()