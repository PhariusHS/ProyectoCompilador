from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showwarning
from tkinter.filedialog import askopenfilename
from os import popen, system, remove
from sys import exit 

user_windows = str(popen("echo %USERNAME%").read()).replace("\n", "")
#window
window = Tk()
window.title("ADC")
window.geometry("1920x1080")


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

    #remplazo keywords
    content = content.replace("MOSTRAR", "print")
    content = content.replace("DICCIONARIO", "dic")
    content = content.replace("LISTA", "list")
    content = content.replace("CLASE", "class")
    content = content.replace("SENO", "sin")
    content = content.replace("COSENO", "cos")
    content = content.replace("INSERTAR", "insert")
    content = content.replace("AGREGAR", "extend")
    content = content.replace("ELIMINAR", "remove")
    content = content.replace("VERDADERO", "true")
    content = content.replace("FALSO", "false")
    content = content.replace("SI", "if")
    content = content.replace("SINO", "else")
    content = content.replace("PARA", "for")
    content = content.replace("MIENTRAS", "while")
    content = content.replace("SINO_ENTONCES", "elif")
    content = content.replace("TAMBIEN", "and")
    content = content.replace("NI", "or")
    content = content.replace("ROMPER", "break")
    content = content.replace("DEVOLVER", "return")

    return content




def compilar():
    pass


def ejecutar():
    archivo = askopenfilename(title="Ejecutar", filetypes=(("academic script" , "*.adc") ,), initialdir="C:/Users/{}/Documents".format(str(user_windows)))
    traduction = traducir(archivo)
    py = open("ejecutador.py", "w")   
    py.write(traduction)
    py.close()
    borrado = popen("cls").read().replace("\n","")
    if borrado.startswith("\"cls\""):
        system("clear")
    else:
        system("cls")
    system("python ejecutador.py")
    remove("ejecutador.py")





#title label
tittle_label = ttk.Label(master = window, text ="Compilador", font=('Comic Sans MS', 36, 'bold italic'))
tittle_label.pack()

#Buttons
buttons_frame = ttk.Frame(master=window)
button = ttk.Button(master=buttons_frame, text = "Ejecutar", command=lambda:ejecutar())
buttons_frame.pack(side = "left")


button.pack()










#Window-run
window.mainloop()