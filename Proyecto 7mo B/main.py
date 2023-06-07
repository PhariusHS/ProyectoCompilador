import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title("DDAAC")
window.geometry("1920x1080")

#title label
tittle_label = ttk.Label(master = window, text ="Compiladorsito :D", font=('Comic Sans MS', 40, 'bold italic'))
tittle_label.pack()

#Buttons
buttons_frame = ttk.Frame(master=window)
button = ttk.Button(master=buttons_frame, text = "First Button(Compile? [img.play])")
buttons_frame.pack(side = "left")
button.pack()

#Main-run
window.mainloop()

