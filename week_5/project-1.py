import tkinter as tk

# Simple employee data
employees = {
    "Logistics": ["Alice", "Bob", "Charlie"],
    "IT": ["Daniel", "Eve"],
    "HR": ["Frank", "Grace"]
}

# Function to check employee
def check_employee():
    name = name_entry.get()
    dept = dept_entry.get()

    if dept in employees and name in employees[dept]:
        result = "Welcome " + name + "!"
    else:
        result = "Sorry, employee not found."

    result_label.config(text=result)

# GUI setup
window = tk.Tk()
window.title("Employee Check")
window.geometry("300x250")
window.configure(bg="lightblue")

# Labels and Entry boxes
tk.Label(window, text="Name:", bg="lightblue", font=("Arial", 10)).pack(pady=2)
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Department:", bg="lightblue", font=("Arial", 10)).pack(pady=2)
dept_entry = tk.Entry(window)
dept_entry.pack()

# Button
tk.Button(window, text="Check", command=check_employee, bg="white", fg="black").pack(pady=10)

# Result Label
result_label = tk.Label(window, text="", justify="left", bg="lightblue", font=("Arial", 10))
result_label.pack()

window.mainloop()
