import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Variables de colores
color_principal = "#7371FC"
color_fondo = "#F2F5FF"
color_texto = "#14080E"
color_texto_secundario = "#34344A"
color_resaltado = "#DB5461"

# Función para publicar un post


def publicar_post():
    contenido = entry_post.get()
    if contenido:
        tiempo_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        texto_post = f"[{tiempo_actual}] {contenido}\n"
        texto_posteo.insert(tk.END, texto_post)
        entry_post.delete(0, tk.END)


# Configuración de la ventana principal
root = tk.Tk()
root.title("BitSocial")
root.geometry("800x600")  # Tamaño personalizado
root.configure(bg=color_principal)
root.iconbitmap('images/x.ico')

# Configuración del título
titulo = tk.Label(root, text="Bienvenido BitSocial", font=(
    "Helvetica", 20), bg=color_principal, fg=color_texto)
titulo.pack(pady=20)

# Avatar del usuario
avatar = tk.PhotoImage(file="public/avatar.png")
avatar_label = tk.Label(root, image=avatar, bg=color_principal)
avatar_label.pack(anchor=NW)

# Nombre del usuario
nombre_usuario = tk.Label(root, text="Nombre de Usuario", font=(
    "Helvetica", 16), bg=color_principal, fg=color_texto)
nombre_usuario.pack()

# Nombre y Apellido
nombre_apellido = tk.Label(root, text="Nombre Apellido", font=(
    "Helvetica", 14), bg=color_principal, fg=color_texto_secundario)
nombre_apellido.pack()

# Entrada de texto para el posteo
entry_post = ttk.Entry(root, width=40)
entry_post.pack(pady=10)

# Botón para publicar un post
btn_publicar = ttk.Button(root, text="Publicar", command=publicar_post)
btn_publicar.pack()

# Área de visualización de los posteos
texto_posteo = tk.Text(root, wrap=tk.WORD, width=60, height=10,
                       bg=color_fondo, fg=color_texto, font=("Helvetica", 12))
texto_posteo.pack(padx=20, pady=20)

# Scrollbar para el área de visualización
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=texto_posteo.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
texto_posteo.config(yscrollcommand=scrollbar.set)

# Iniciar la aplicación
root.mainloop()
