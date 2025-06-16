import tkinter as tk

def button_click():
    msgbox.showinfo("Info," "Welcome to cos102 GUI class")

    result = msgbox.askyesno("Do you want to continue?")

    root = tk.Tk()
    root.title = ("GUI app")
    root.geometry = ("400x600")

    label = tk.Label(root, text = ("Hello bro"))
    label.pack()

    button = tk.Button(root, text = ("Click Me!"), command = button_click)
    button.pack()
    button.config(fg="red", bg="blue")

    root.mainloop
