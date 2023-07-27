import tkinter as tk
from tkinter import messagebox
import datetime

# Create the main window
window = tk.Tk()
window.title("Future Day Calculator")

# Function to calculate the future day and date
def calculate_future_day():
    try:
        days = int(days_entry.get())
        current_date = datetime.datetime.now()
        future_date = current_date + datetime.timedelta(days=days)
        day_of_week = future_date.strftime("%A")
        date = future_date.strftime("%Y-%m-%d")
        messagebox.showinfo("Future Day", f"{days} days from now will be a {day_of_week} ({date}).")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number of days.")

# Create the days entry and button
days_label = tk.Label(window, text="Days:", font=("Arial", 12))
days_label.pack(padx=10, pady=5)

days_entry = tk.Entry(window, width=10)
days_entry.pack(padx=10, pady=5)

calculate_button = tk.Button(window, text="Calculate", command=calculate_future_day)
calculate_button.pack(padx=10, pady=5)

# Start the main event loop
window.mainloop()
