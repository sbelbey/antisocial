usuario = {
    "nombre": "",
}

def configurar_usuario(nombre):
    usuario["nombre"] = nombre

def mostrar_usuario():
    print("Nombre:", usuario["nombre"])

print("Bienvenido a nuestra red social")
nombre = input("Ingresa tu nombre: ")

configurar_usuario(nombre)
print("\nNombre del usuario:")
mostrar_usuario()