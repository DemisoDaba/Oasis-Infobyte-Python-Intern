import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt

# BMI Calculator Functions
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Main Functionality
def calculate_and_display():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and height must be positive numbers.")
            return
        
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        result_label.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")
        
        # Data storage for advanced level
        save_data(weight, height, bmi)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numerical values.")

# Advanced Level: Data Storage
def create_table():
    conn = sqlite3.connect("bmi_data.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bmi_records
                 (id INTEGER PRIMARY KEY, weight REAL, height REAL, bmi REAL)''')
    conn.commit()
    conn.close()

def save_data(weight, height, bmi):
    conn = sqlite3.connect("bmi_data.db")
    c = conn.cursor()
    c.execute("INSERT INTO bmi_records (weight, height, bmi) VALUES (?, ?, ?)", (weight, height, bmi))
    conn.commit()
    conn.close()

def plot_bmi_trend():
    conn = sqlite3.connect("bmi_data.db")
    c = conn.cursor()
    c.execute("SELECT bmi FROM bmi_records")
    data = c.fetchall()
    conn.close()
    
    if data:
        bmi_values = [record[0] for record in data]
        plt.plot(bmi_values)
        plt.xlabel("Record Number")
        plt.ylabel("BMI")
        plt.title("BMI Trend Over Time")
        plt.show()
    else:
        messagebox.showinfo("Info", "No BMI data available.")

# GUI Initialization
root = tk.Tk()
root.title("BMI Calculator")

weight_label = tk.Label(root, text="Enter your weight (kg):")
weight_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

height_label = tk.Label(root, text="Enter your height (m):")
height_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_and_display)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Advanced Level: Data Storage Buttons
create_table()
view_data_button = tk.Button(root, text="View BMI Trend", command=plot_bmi_trend)
view_data_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

root.mainloop()
