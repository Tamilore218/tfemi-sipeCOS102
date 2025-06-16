import tkinter as tk 
from tkinter import messagebox

class Delivery:
    def __init__(self, location):
        self.location = location   

    def set_weight(self, weight):
        self.weight = weight  

    def calculate_price(self):
        if self.location.lower() == "pau":
            if self.weight >= 10:
                return 2000
            else:
                return 1500

        elif self.location.lower() == "epe":
            if self.weight >= 10:
                return 5000
            else:
                return 4000

        else:
            return None  
window = tk.Tk()
window.title("Delivery Service Calculator")
window.geometry("400x250")

label_location = tk.Label(window, text="Enter your location (PAU OR EPE)", font=("Arial", 16))
label_location.pack(pady=10)
entry_location = tk.Entry(window, width=40, font=("Arial", 16))
entry_location.pack(pady=10)

label_weight = tk.Label(window, text="Enter the weight of your package.", font=("Arial", 16))
label_weight.pack(pady=10)
entry_weight = tk.Entry(window, width=40, font=("Arial", 16))
entry_weight.pack(pady=10)

def calculate_cost():
    location = entry_location.get
    weight = entry_weight.get

    weight = float(weight)

    delivery = Delivery(location)
    delivery.set_weight(weight)
    cost = Delivery.calculate_price()

    if cost != None:
        messagebox.showinfo("The cost of this delivery is ₦" + str(cost))
    else:
        messagebox.showinfo("Invalid location")    



    

    




