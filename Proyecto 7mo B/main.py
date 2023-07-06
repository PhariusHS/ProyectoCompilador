# Import
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
import ctypes
import sys
from tkinter import ttk
from tkinter.messagebox import showwarning
from tkinter.filedialog import askopenfilename
from os import popen, system, remove
from sys import exit 
from threading import Thread
import tkinter as tk
from idlelib.percolator import Percolator
import idlelib.colorizer as ic


nofileOpenedString = 'New File'
currentFilePath = nofileOpenedString
fileTypes = [("academic script" , "*.adc")]
user_windows = str(popen("echo %USERNAME%").read()).replace("\n", "")

# Tkinter Setup
window = Tk()

window.title("ADC" + " - " + currentFilePath)

# Window 
window.geometry('720x480')

# Set the first column to occupy 100% of the width
window.grid_columnconfigure(0, weight=1)



# Checkeo si existe python dentro de la pc
python_download = popen("python --version")

if str(python_download).startswith("\"python\""):
    showwarning("Se necesita una version de python", "para utilizar este lenguaje descarga la version de python mas reciente")
    window.destroy()
    exit()


def MenuArchivoHandeler(action):
    global currentFilePath

    # Abrir archivo
    if action == "Abrir":
        file = filedialog.askopenfilename(filetypes=fileTypes)
        window.title("ADC" + " - " + file)
        currentFilePath = file
        with open(file, 'r') as f:
            txt.delete(1.0, END)
            txt.insert(INSERT, f.read())

    # Archivo nuevo
    elif action == "Nuevo":
        currentFilePath = nofileOpenedString
        txt.delete(1.0, END)
        window.title("ADC" + " - " + currentFilePath)

    # Guardado
    elif action == "Guardar" or action == "Guardar Como":
        if currentFilePath == nofileOpenedString or action == 'Guardar Como':
            currentFilePath = filedialog.asksaveasfilename(filetypes=fileTypes)
        with open(currentFilePath, 'w') as f:
            f.write(txt.get('1.0', 'end'))
        window.title("ADC" + " - " + currentFilePath)


def textchange(event):
    window.title("ADC" + " - *" + currentFilePath)
    
# Text Area
txt_frame = Frame(window)
txt_frame.grid(row=1, column=0, sticky=N+S+E+W)

txt = scrolledtext.ScrolledText(txt_frame, height=10)
txt.pack(side=LEFT, fill=BOTH, expand=True)


# acomodado de barra y cuadro de texto
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

# Bind event in the widget to a function
txt.bind('<KeyPress>', textchange)

# Menu
menu = Menu(window)

MenuArchivo = Menu(menu, tearoff=False)

# Comandos
MenuArchivo.add_command(label='Nuevo', accelerator="Ctrl+N", command=lambda: MenuArchivoHandeler("Nuevo"))
MenuArchivo.add_command(label='Abrir', accelerator="Ctrl+A", command=lambda: MenuArchivoHandeler("Abrir"))

# Separador
MenuArchivo.add_separator()
MenuArchivo.add_command(label='Guardar', accelerator="Ctrl+G", command=lambda: MenuArchivoHandeler("Guardar"))
MenuArchivo.add_command(label='Guardar Como', accelerator="Ctrl+Shift+G", command=lambda: MenuArchivoHandeler("Guardar Como"))

menu.add_cascade(label='Archivo', menu=MenuArchivo)
# Ejecutar
menu.add_checkbutton(label='Ejecutar', command=lambda:ejecutar())
# Set Menu 
window.config(menu=menu)
#binds

txt.bind("<Control-g>", lambda event: MenuArchivoHandeler("Guardar"))
txt.bind("<Control-G>", lambda event: MenuArchivoHandeler("Guardar Como"))
txt.bind("<Control-a>", lambda event: MenuArchivoHandeler("Abrir"))
txt.bind("<Control-n>", lambda event: MenuArchivoHandeler("Nuevo"))


if len(sys.argv) == 2:
    currentFilePath = sys.argv[1]
    window.title("ADC" + " - " + currentFilePath)
    with open(currentFilePath, 'r') as f:
        txt.delete(1.0,END)
        txt.insert(INSERT,f.read())
        
        
#Functions
def traducir(archivo=currentFilePath.format(str(user_windows))):
    archivo_abierto = open(archivo, "r")
    content = archivo_abierto.read()
    archivo_abierto.close()

    #Remplazo keyword basicas
    content = content.replace("MOSTRAR", "print")
    content = content.replace("ENTERO", "int")
    content = content.replace("DECIMAL", "float")
    content = content.replace("TEXTO", "string")
    content = content.replace("DICCIONARIO", "dic")
    content = content.replace("LISTA", "list")
    content = content.replace("CLASE", "class")
    content = content.replace("SENO", "sin")
    content = content.replace("COSENO", "cos")
#Keywords avanzadas
    content = content.replace("NADA","none")
    content = content.replace("INSERTAR", "insert")
    content = content.replace("AGREGAR", "extend")
    content = content.replace("ELIMINAR", "remove")
    content = content.replace("BORRAR", "del")
    content = content.replace("INTENTA","try")
    content = content.replace("EXCEPTO","except")
    content = content.replace("FINALMENTE","finally")
    content = content.replace("VERDADERO", "true")
    content = content.replace("FALSO", "false")
    content = content.replace("SINO_ENTONCES", "elif")
    content = content.replace("SINO", "else")
    content = content.replace("SI", "if")
    content = content.replace("PARA", "for")
    content = content.replace("MIENTRAS", "while")
    content = content.replace("TAMBIEN", "and")
    content = content.replace("NI", "or")
    content = content.replace("ROMPER", "break")
    content = content.replace("DEVOLVER", "return")
    return content




def compilar():
    pass


#Ejecucion y lectura de archivos ".adc" como ".py"
def ejecutar():
    archivo = currentFilePath.format(str(user_windows))
    traduction = traducir(archivo)
    py = open("ejecutador.py", "w")   
    py.write(traduction)
    py.close()
    #borrado de consola previa
    borrado = popen("cls").read().replace("\n","")
    if borrado.startswith("\"cls\""):
        system("clear")
    else:
        system("cls")



    system("py ejecutador.py")
    remove("ejecutador.py")

#cosa para los colores
Percolator(txt).insertfilter(ic.ColorDelegator())
# Main Loop
window.mainloop()