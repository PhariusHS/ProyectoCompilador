from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showwarning
from tkinter.filedialog import askopenfilename
from os import popen, system, remove
from sys import exit 
from threading import Thread
import tkinter as tk
from idlelib.percolator import Percolator
import idlelib.colorizer as ic

user_windows = str(popen("echo %USERNAME%").read()).replace("\n", "")
#window
window = Tk()
window.title("ADC")
window.geometry("720x480")


#Checkeo si existe python dentro de la pc
python_download = popen("python --version")

if str(python_download).startswith("\"python\""):
    showwarning("Se necesita una version de python", "para utilizar este lenguaje descarga la version de python mas reciente")
    window.destroy()
    exit()



#Functions
def traducir(archivo="C:/Users/{}/Documents/adc.adc".format(str(user_windows))):
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
    archivo = askopenfilename(title="Ejecutar", filetypes=(("academic script" , "*.adc") ,), initialdir="C:/Users/{}/Documents".format(str(user_windows)))
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





#title label
tittle_label = ttk.Label(master = window, text ="Compilador", font=('Comic Sans MS', 36, 'bold italic'))
tittle_label.pack()

#Buttons label
buttons_frame = ttk.Frame(master=window)
#Buttons
button = ttk.Button(master=buttons_frame, text = "Ejecutar", command=lambda:ejecutar())
buttons_frame.pack(side = "left")
#editor texto
text = tk.Text(window)
Percolator(text).insertfilter(ic.ColorDelegator())


text.pack()
button.pack()
#Window-run
window.mainloop()

