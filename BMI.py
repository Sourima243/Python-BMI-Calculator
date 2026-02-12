# ===== BMI Calculator GUI Project =====

import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Enter positive values only!")
            return

        bmi = weight / (height ** 2)
        category = get_category(bmi)

        result_label.config(text=f"BMI = {bmi:.2f}  |  {category}")
        save_data(weight, height, bmi, category)

    except ValueError:
        messagebox.showerror("Error", "Enter numeric values only!")

# BMI Category Function
def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Save data to CSV file
def save_data(weight, height, bmi, category):
    with open("bmi_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), weight, height, bmi, category])

# GUI Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x300")
root.configure(bg="lightblue")

# Title
tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

# Weight Input
tk.Label(root, text="Weight (kg):", bg="lightblue").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# Height Input
tk.Label(root, text="Height (meters):", bg="lightblue").pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Calculate Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="green", fg="white").pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Enter details to calculate BMI", font=("Arial", 12), bg="lightblue")
result_label.pack()

root.mainloop()
