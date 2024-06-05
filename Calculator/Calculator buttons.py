import tkinter as tk
from tkinter import messagebox
from tkinter import font

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        
        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

#Larger buttons
large_font = font.Font(family="Helvetica", size=20, weight = "bold")
medium_font = font.Font(family="helvetica", size=18)

# Create and place the entry widgets
entry1 = tk.Entry(root, width=20,font=medium_font)
entry1.grid(row=0, column=1)

entry2 = tk.Entry(root, width=20,font=medium_font)
entry2.grid(row=1, column=1)

# Create and place the labels
tk.Label(root, text="First Number:").grid(row=0, column=0)
tk.Label(root, text="Second Number:").grid(row=1, column=0)

# Create and place the result label correctly
result_label = tk.Label(root, text="Result:")
result_label.grid(row=2, columnspan=2)

# Create and place the buttons
tk.Button(root, text="Add", command=lambda: calculate('add'), font=medium_font, width=10, height=2).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Subtract", command=lambda: calculate('subtract'), font=medium_font, width=10, height=2).grid(row=3, column=1, padx=10, pady=10)
tk.Button(root, text="Multiply", command=lambda: calculate('multiply'), font=medium_font, width=10, height=2).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Divide", command=lambda: calculate('divide'), font=medium_font, width=10, height=2).grid(row=4, column=1, padx=10, pady=10)
# Run the application
root.mainloop()
