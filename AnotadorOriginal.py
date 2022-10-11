#!/usr/bin/python3

from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import messagebox

ruta = ""

def AcercaDe(event):
    messagebox.showinfo("Acerca de", message = """
Anotador hecho por Paty
2021
Version v0.1
    """)

def Ayuda(event):
    messagebox.showinfo("Ayuda", message = """
Comandos de Archivo

    Ctrl + n: Nuevo
    Ctrl + a: Abrir
    Ctrl + s: Guardar
    Ctrl + Shift + s: Guardar Como
    Ctrl + q: Salir

General

    Ctrl + h: Ayuda
    Ctrl + Shift + h: Acerca De
    """)

def Nuevo(event):
    global ruta

    if ruta != "":
        Guardar("Control-s")

    texto.delete(1.0, END)
    raiz.title("Anotador")
    ruta = ""
    var.set("Archivo nuevo")

def Abrir(event):
    global ruta

    ruta = FileDialog.askopenfilename(initialdir = ".", filetypes = (("Archivos de texto", "*.txt"),), title = "Abrir un Archivo")

    if ruta != "":
        fichero = open(ruta, "r")
        contenido = fichero.read()
        texto.delete(1.0, "end")
        texto.insert("insert", contenido)
        fichero.close()
        raiz.title("Anotador")
        var.set(ruta)

def Guardar(event):
    global ruta

    if ruta != "":
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        var.set("Archivo guardado")
    else:
        GuardarComo("Control-a")

def GuardarComo(event):
    global ruta
    fichero = FileDialog.asksaveasfile(title = "Guardar Archivo", mode = "w", defaultextension = ".txt")
    ruta = fichero.name

    if fichero is not None:
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        var.set("Archivo guardado")


def Salir(event):
    ventanaSalir = Toplevel(width = 210, height = 100)
    ventanaSalir.title("Salir")
    ventanaSalir.minsize(210, 100)
    ventanaSalir.resizable(0, 0)
    ventanaSalir.grab_set()
    ventanaSalir.transient(raiz)
    salirTexto = Label(ventanaSalir, text = "¿Desea guardar antes de salir?").grid(row = 0, column = 0, sticky = "ew", padx = 15)
    salirSiBoton = Button(ventanaSalir, text = "Guardar", command = SalirGuardar).grid(row = 1, column = 0, sticky = "ew", padx = 15)
    salirNoBoton = Button(ventanaSalir, text = "Salir sin guardar", command = SalirSinGuardar).grid(row = 2, column = 0, sticky = "ew", padx = 15)

def SalirGuardar():
    Guardar("Control-s")
    raiz.quit()

def SalirSinGuardar():
    raiz.quit()

def Cerrando():
    Salir("Control-q")

raiz = Tk()
notaGuardada = StringVar()
var = StringVar()
var.set("Hola wenas")
foto = PhotoImage(file = "ico.png")

frame = Frame(raiz)
barraMenu = Menu(frame)
texto = Text(frame, width = 30, height = 10)
mensajes = Label(frame, textvariable = var, justify = LEFT)

raiz.title("Anotador")
raiz.config(menu = barraMenu)
raiz.resizable(1, 1)
raiz.minsize(300, 250)
raiz.option_add('*font', '{Helvetica} 11')
raiz.iconphoto(False, foto)

frame.pack(fill = "both", expand = "true")

menuArchivo = Menu(barraMenu, tearoff = 0)
menuArchivo.add_command(label = "Nuevo", command = lambda: Nuevo("Control-n"))
menuArchivo.add_command(label = "Abrir", command = lambda: Abrir("Control-A"))
menuArchivo.add_command(label = "Guardar", command = lambda: Guardar("Control-s"))
menuArchivo.add_command(label = "Guardar como", command = lambda: GuardarComo("Control-Shift-s"))
menuArchivo.add_separator()
menuArchivo.add_command(label = "Salir", command = lambda: Salir("Control-q"))

'''
menuEditar = Menu(barraMenu, tearoff = 0)
menuEditar.add_command(label = "Cortar", command = lambda: Cortar)
menuEditar.add_command(label = "Copiar", command = lambda: Copiar)
menuEditar.add_command(label = "Pegar", command = lambda: Pegar)
'''

menuAyuda = Menu(barraMenu, tearoff = 0)
menuAyuda.add_command(label = "Ayuda", command = lambda: Ayuda("Control-h"))
menuAyuda.add_separator()
menuAyuda.add_command(label = "Acerca de", command = lambda: AcercaDe("Control-Shift-h"))

barraMenu.add_cascade(label = "Archivo", menu = menuArchivo)
#barraMenu.add_cascade(label = "Editar", menu = menuEditar)
barraMenu.add_cascade(label = "Ayuda", menu = menuAyuda)

texto.pack(fill = "both", expand = "true")
texto.config(bg = "#F9E79F")

mensajes.pack()

raiz.bind_all("<Control-q>", Salir)
raiz.bind_all("<Control-Q>", Salir)
raiz.bind_all("<Control-n>", Nuevo)
raiz.bind_all("<Control-N>", Nuevo)
raiz.bind_all("<Control-a>", Abrir)
raiz.bind_all("<Control-A>", Abrir)
raiz.bind_all("<Control-s>", Guardar)
raiz.bind_all("<Control-S>", Guardar)
raiz.bind_all("<Control-Shift-s>", GuardarComo)
raiz.bind_all("<Control-Shift-S>", GuardarComo)
raiz.bind_all("<Control-h>", Ayuda)
raiz.bind_all("<Control-H>", Ayuda)
raiz.bind_all("<Control-Shift-h>", AcercaDe)
raiz.bind_all("<Control-Shift-H>", AcercaDe)

raiz.protocol("WM_DELETE_WINDOW", Cerrando)
raiz.mainloop()

# Fuente: https://docs.hektorprofe.net/python/interfaces-graficas-con-tkinter/editor-de-texto/
