import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
import ttkbootstrap as tb
import webbrowser


# Read TSV files
def read_tsv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t', fieldnames=['food_id', 'food_name'])
        return [row for row in reader]


def read_table(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file, delimiter='\t')
        return [row for row in reader]


# Write export TSV file
def write_tsv(file_path, data, headers):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)


# Read food details
def read_food_details(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        return {rows[0]: float(rows[1]) for rows in reader if rows[1].replace('.', '', 1).isdigit()}


# Load food name and ID correspondence
name_foodID_correspondence = read_tsv('name_foodID_correspondence.tsv')
food_id_map = {row['food_name']: row['food_id'] for row in name_foodID_correspondence}
# Sort food names for easier access to the dropdown menu
sorted_food_names = sorted(food_id_map.keys())
# Load blank table for micronutrients
blank_table = read_table('blank_table.tsv')
micronutrient_list = [row['nutrients'] for row in blank_table]
# Initialize micronutrient totals to 0
micronutrient_totals = {micronutrient: 0.0 for micronutrient in micronutrient_list}
added_foods = []

# Sequential food addition
def add_food():
    food_name = food_var.get()
    try:
        quantity = float(quantity_var.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for quantity.")
        return
    
    # Missing food from database shouldn't happen but let's be sure to throw an error in case of missing database files
    if food_name not in food_id_map:
        messagebox.showerror("Error", "Food not found in the database.")
        return

    food_id = food_id_map[food_name]
    try:
        food_details = read_food_details(f'food_details/{food_id}')
    except FileNotFoundError:
        messagebox.showerror("Error", f"Details file for food ID {food_id} not found.")
        return
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while reading the food details: {e}")
        return
    
    # Sum the proportional total
    for micronutrient in micronutrient_totals:
        if micronutrient in food_details:
            micronutrient_totals[micronutrient] += (food_details[micronutrient] * (quantity / 100.0))

    messagebox.showinfo("Info", f"Added {quantity}g of {food_name}")
    added_foods.append((food_name, quantity))
    update_added_foods_list()


def update_added_foods_list():
    for widget in added_foods_frame.winfo_children():
        widget.destroy()
    
    for i, (food_name, quantity) in enumerate(added_foods):
        frame = tk.Frame(added_foods_frame)
        frame.pack(anchor='w')
        tk.Label(frame, text=f"{food_name} - {quantity}g").pack(side='left')
        tk.Button(frame, text="Delete", command=lambda i=i: delete_food(i)).pack(side='right')


def delete_food(index):
    food_name, quantity = added_foods.pop(index)
    food_id = food_id_map[food_name]
    food_details = read_food_details(f'food_details/{food_id}')
    
    for micronutrient in micronutrient_totals:
        if micronutrient in food_details:
            micronutrient_totals[micronutrient] -= (food_details[micronutrient] * (quantity / 100.0))
    
    messagebox.showinfo("Info", f"Removed {quantity}g of {food_name}")
    update_added_foods_list()


def search_foods(event):
    search_term = search_var.get()
    matching_foods = [food for food in sorted_food_names if search_term.lower() in food.lower()]
    food_menu['values'] = matching_foods


# Get the data
def export_data():
    file_path = filedialog.asksaveasfilename(defaultextension=".tsv", filetypes=[("TSV files", "*.tsv")])
    if not file_path:
        return

    data_to_export = [{'micronutrient': k, 'total_amount': v} for k, v in micronutrient_totals.items()]
    headers = ['micronutrient', 'total_amount']
    write_tsv(file_path, data_to_export, headers)
    messagebox.showinfo("Info", f"Data exported to {file_path}")


# Wipe and reset
def wipe_data():
    if messagebox.askyesno("Confirm Wipe", "Are you sure you want to wipe all data? Unsaved data will be lost."):
        global micronutrient_totals, added_foods
        micronutrient_totals = {micronutrient: 0.0 for micronutrient in micronutrient_list}
        added_foods = []
        update_added_foods_list()
        food_var.set('')
        quantity_var.set('')


# Infotab
def show_info():
    info_text = ("NutriTable CREAtion\n"
                 "Version: 1.0\n"
                 "Maintainer: Fabbrini Marco\n"
                 "Contact: fabbrinimarco.mf@gmail.com\n"
                 "\n"
                 "For usage instructions, visit:\n"
                 "https://github.com/FabbriniMarco/NutriTable-CREAtion\n"
                 "\n"
                 "The CREA database used from this tool can be consulted at:\n"
                 "https://www.alimentinutrizione.it/sezioni/tabelle-nutrizionali\n"
                 "\n"
                 "We thank the Italian Council for Agricultural Research and Analysis of Agricultural Economic workgroup for their efforts in profiling foods\n"
                 "https://www.alimentinutrizione.it/gruppo-di-lavoro")

    messagebox.showinfo("Program Info", info_text)


def open_github():
    webbrowser.open_new("https://github.com/FabbriniMarco/NutriTable-CREAtion")


def open_crea():
    webbrowser.open_new("https://www.alimentinutrizione.it/sezioni/tabelle-nutrizionali")


# Tk/tb
root = tb.Window(themename="sandstone")  
root.title("NutriTable CREAtion")
root.geometry("900x550")  

# Widgets
food_var = tk.StringVar()
quantity_var = tk.StringVar()
search_var = tk.StringVar()

main_frame = tb.Frame(root)
main_frame.pack(expand=True, fill='both')

tb.Label(main_frame, text="Select Food:").pack(pady=5)
food_menu = tb.Combobox(main_frame, textvariable=food_var, values=sorted_food_names, width=50)
food_menu.pack(pady=5)

tb.Label(main_frame, text="Search Food:").pack(pady=5)
search_entry = tb.Entry(main_frame, textvariable=search_var, width=50)
search_entry.pack(pady=5)
search_entry.bind('<KeyRelease>', search_foods)

tb.Label(main_frame, text="Enter Quantity (grams):").pack(pady=5)
quantity_entry = tb.Entry(main_frame, textvariable=quantity_var, width=50)
quantity_entry.pack(pady=5)

add_button = tb.Button(main_frame, text="Add Food", command=add_food)
add_button.pack(pady=10)

tb.Label(main_frame, text="Added Foods:").pack(pady=5)
added_foods_frame = tb.Frame(main_frame)
added_foods_frame.pack(pady=5)

export_button = tb.Button(main_frame, text="Export Data", command=export_data)
export_button.pack(pady=10)

wipe_button = tb.Button(main_frame, text="Wipe Data", command=wipe_data)
wipe_button.pack(pady=10)

button_frame = tb.Frame(main_frame)
button_frame.pack(pady=10)

info_button = tb.Button(button_frame, text="Info", command=show_info, bootstyle='secondary')
info_button.pack(side="left", padx=5)

website1_button = tb.Button(button_frame, text="Github", command=open_github, bootstyle='secondary')
website1_button.pack(side="left", padx=5)

website2_button = tb.Button(button_frame, text="CREA database", command=open_crea, bootstyle='secondary')
website2_button.pack(side="left", padx=5)

# Run
root.mainloop()
# Version 1.0 - May 2024 - MF