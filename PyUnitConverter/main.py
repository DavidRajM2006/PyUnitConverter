import tkinter as tk
from tkinter import ttk, messagebox
from converter import length, weight, temperature

root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x350")
root.resizable(False, False)

options = {
    "Length": ["cm to m", "m to cm", "km to m", "m to km", "inch to cm", "cm to inch", "feet to m", "m to feet"],
    "Weight": ["g to kg", "kg to g", "lb to kg", "kg to lb", "g to lb", "lb to g"],
    "Temperature": ["C to F", "F to C", "C to K", "K to C", "F to K", "K to F"]
}

def convert():
    try:
        val = float(entry_value.get())
        conv_type = combo_type.get()
        conv_unit = combo_unit.get()
        if conv_type == "Length":
            result = length.convert(val, conv_unit)
        elif conv_type == "Weight":
            result = weight.convert(val, conv_unit)
        elif conv_type == "Temperature":
            result = temperature.convert(val, conv_unit)
        else:
            result = "Invalid Conversion"
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

tk.Label(root, text="Enter Value:").pack(pady=5)
entry_value = tk.Entry(root, width=20)
entry_value.pack(pady=5)

tk.Label(root, text="Select Type:").pack(pady=5)
combo_type = ttk.Combobox(root, values=list(options.keys()), state="readonly")
combo_type.pack(pady=5)

tk.Label(root, text="Select Conversion:").pack(pady=5)
combo_unit = ttk.Combobox(root, values=[], state="readonly")
combo_unit.pack(pady=5)

def update_units(event):
    combo_unit['values'] = options.get(combo_type.get(), [])
    combo_unit.current(0)

combo_type.bind("<<ComboboxSelected>>", update_units)

tk.Button(root, text="Convert", command=convert).pack(pady=10)
label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=10)

root.mainloop()