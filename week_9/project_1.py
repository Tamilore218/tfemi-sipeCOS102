import tkinter as tk
from tkinter import messagebox

# ======= Parent Class =======
class Zenith:
    def __init__(self, name):
        self.name = name

    def mutual_services(self):
        return [
            "Lines of credit",
            "Investment management and accounts",
            "Insurance"
        ]

    def unique_services(self):
        return []

# ======= Subclasses =======
class RetailBanking(Zenith):
    def unique_services(self):
        return [
            "Retirement and education accounts",
            "Loans and mortgages",
            "Checking and saving"
        ]

class GlobalBanking(Zenith):
    def mutual_services(self):
        # Override with no mutual services
        return []

    def unique_services(self):
        return [
            "Multi-currency management services and products",
            "Foreign currency accounts",
            "Foreign currency credit cards",
            "Transborder advisory services",
            "Liquidity management"
        ]

class CommercialBanking(Zenith):
    def unique_services(self):
        return [
            "Advisory services"
        ]

# ======= GUI Application =======
def show_services():
    name = name_entry.get()
    division = division_var.get()

    if not name or not division:
        messagebox.showwarning("Input Error", "Please enter name and select division.")
        return

    if division == "Retail":
        employee = RetailBanking(name)
    elif division == "Global":
        employee = GlobalBanking(name)
    elif division == "Commercial":
        employee = CommercialBanking(name)
    else:
        messagebox.showerror("Division Error", "Invalid division selected.")
        return

    # Collect services
    mutual = employee.mutual_services()
    unique = employee.unique_services()

    services_text = f"Employee: {employee.name}\nDivision: {division}\n\nMutual Services:\n"
    services_text += "\n".join(f"- {service}" for service in mutual)
    services_text += "\n\nUnique Services:\n"
    services_text += "\n".join(f"- {service}" for service in unique)

    result_box.config(state='normal')
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, services_text)
    result_box.config(state='disabled')

# ======= Tkinter GUI Setup =======
window = tk.Tk()
window.title("Zenith Bank - Division Services")
window.geometry("400x500")

tk.Label(window, text="Enter Employee Name:").pack(pady=5)
name_entry = tk.Entry(window)
name_entry.pack(pady=5)

tk.Label(window, text="Select Division:").pack(pady=5)
division_var = tk.StringVar()
division_menu = tk.OptionMenu(window, division_var, "Retail", "Global", "Commercial")
division_menu.pack(pady=5)

tk.Button(window, text="Show Services", command=show_services).pack(pady=10)

result_box = tk.Text(window, height=20, width=45, wrap="word", state='disabled')
result_box.pack(pady=10)

window.mainloop()
