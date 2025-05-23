import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero!")
                return
        else:
            messagebox.showerror("Error", "Invalid operation selected!")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Input fields
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Operation dropdown
tk.Label(root, text="Select operation:").pack()
operation_var = tk.StringVar(root)
operation_var.set('+')  # default operation
tk.OptionMenu(root, operation_var, '+', '-', '*', '/').pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Start the GUI event loop
root.mainloop()
