import tkinter as tk
import os


def main():
    root = tk.Tk()
    root.title('AntiSocial')
    root.resizable(0, 0)

    frame = tk.Frame(root)
    frame.pack()
    frame.config(width=1024, height=800, bg='blue')

    root.mainloop()


if __name__ == '__main__':
    main()
