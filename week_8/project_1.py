import tkinter as tk
from tkinter import messagebox
import random

# List of employees
employees = [
    "Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu",
    "Stella Mankinde", "Jane Akibo", "Ago James", "Michell Taiwo", "Abraham Jones",
    "Nicole Anide", "Kosi Korso", "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"
]

# List of tasks
tasks = ["Loading", "Transporting", "Reviewing Orders", "Customer Service", "Delivering Items"]

# OOP Class for employee
class Employees:
    def __init__(self, name):
        self.name = name
        self.attendance = False
        self.task = None

    def is_employee_valid(self):
        return self.name in employees
    
    def take_attendance(self):
        self.attendance = True

    def assign_task(self):
        self.task = random.choice(tasks)

# Function triggered by button
def verify_employee():
    name = entry_name.get()
    emp = Employees(name)

    if emp.is_employee_valid():
        emp.take_attendance()
        emp.assign_task()
        messagebox.showinfo("Access Granted", f"Welcome, {emp.name}!\nAttendance Marked ✅\nTask Assigned: {emp.task}")
    else:
        messagebox.showwarning("Access Denied", f"Sorry, {emp.name}. You are not authorized ❌")

# GUI setup
window = tk.Tk()
window.title("Employee Identity and Task System")  # FIXED: .title is a function
window.geometry("400x250")                         # FIXED: .geometry is a function

# GUI widgets
label_title = tk.Label(window, text="Enter your full name", font=("Arial", 16))
label_title.pack(pady=10)

entry_name = tk.Entry(window, width=40, font=("Arial", 16))
entry_name.pack(pady=5)

verify_button = tk.Button(window, text="Verify and Assign Task", font=("Arial", 16), command=verify_employee)
verify_button.pack(pady=20)

# Start the GUI loop
window.mainloop()
