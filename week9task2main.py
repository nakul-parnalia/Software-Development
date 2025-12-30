import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

FILE_NAME = "store_gui.json"

DEFAULT_ITEMS = [
    {"id": 1, "name": "Rice", "price": 50, "quantity": 20},
    {"id": 2, "name": "Sugar", "price": 40, "quantity": 15},
    {"id": 3, "name": "Oil", "price": 120, "quantity": 10},
    {"id": 4, "name": "Milk", "price": 30, "quantity": 25},
    {"id": 5, "name": "Bread", "price": 25, "quantity": 18},
    {"id": 6, "name": "Eggs", "price": 6, "quantity": 50},
    {"id": 7, "name": "Soap", "price": 35, "quantity": 30},
]


def load_items():
    if not os.path.exists(FILE_NAME):
        return DEFAULT_ITEMS.copy()
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_items():
    with open(FILE_NAME, "w") as file:
        json.dump(items, file, indent=4)


def refresh_table():
    for row in table.get_children():
        table.delete(row)
    for item in items:
        table.insert("", "end", values=(item["id"], item["name"], item["price"], item["quantity"]))


def add_item():
    try:
        name = name_entry.get()
        price = float(price_entry.get())
        qty = int(qty_entry.get())

        if not name:
            raise ValueError

        new_id = max(item["id"] for item in items) + 1
        items.append({"id": new_id, "name": name, "price": price, "quantity": qty})
        save_items()
        refresh_table()
        messagebox.showinfo("Success", "Item added successfully")
    except:
        messagebox.showerror("Error", "Invalid input")


def update_item():
    selected = table.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select an item")
        return

    item_id = int(table.item(selected)["values"][0])
    qty = int(qty_entry.get())

    for item in items:
        if item["id"] == item_id:
            item["quantity"] = qty
            save_items()
            refresh_table()
            messagebox.showinfo("Updated", "Quantity updated")


def sell_item():
    selected = table.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select an item")
        return

    item_id = int(table.item(selected)["values"][0])
    sell_qty = int(qty_entry.get())

    for item in items:
        if item["id"] == item_id:
            if sell_qty > item["quantity"]:
                messagebox.showerror("Error", "Insufficient stock")
                return
            item["quantity"] -= sell_qty
            save_items()
            refresh_table()
            messagebox.showinfo("Sale", "Item sold successfully")


def delete_item():
    selected = table.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select an item")
        return

    item_id = int(table.item(selected)["values"][0])
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            save_items()
            refresh_table()
            messagebox.showinfo("Deleted", "Item removed")


# GUI Setup
root = tk.Tk()
root.title("Store Inventory Manager")
root.geometry("650x450")

items = load_items()

# Table
table = ttk.Treeview(root, columns=("ID", "Name", "Price", "Qty"), show="headings")
for col in ("ID", "Name", "Price", "Qty"):
    table.heading(col, text=col)
table.pack(fill="x", padx=10, pady=10)

# Inputs
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0)
tk.Label(frame, text="Price").grid(row=0, column=2)
tk.Label(frame, text="Quantity").grid(row=0, column=4)

name_entry = tk.Entry(frame)
price_entry = tk.Entry(frame)
qty_entry = tk.Entry(frame)

name_entry.grid(row=0, column=1)
price_entry.grid(row=0, column=3)   
qty_entry.grid(row=0, column=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Item", command=add_item).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update Qty", command=update_item).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Sell Item", command=sell_item).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Delete Item", command=delete_item).grid(row=0, column=3, padx=5)

refresh_table()
root.mainloop()
