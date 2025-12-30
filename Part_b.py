import json
import os

FILE_NAME = "store_items.json"


def load_items():
    if not os.path.exists(FILE_NAME):
        return [
            {"id": 1, "name": "Rice", "price": 50, "quantity": 20},
            {"id": 2, "name": "Sugar", "price": 40, "quantity": 15},
            {"id": 3, "name": "Oil", "price": 120, "quantity": 10},
            {"id": 4, "name": "Milk", "price": 30, "quantity": 25},
            {"id": 5, "name": "Bread", "price": 25, "quantity": 18},
            {"id": 6, "name": "Eggs", "price": 6, "quantity": 50},
            {"id": 7, "name": "Soap", "price": 35, "quantity": 30}
        ]
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error loading data. Starting with default items.")
        return []


def save_items(items):
    with open(FILE_NAME, "w") as file:
        json.dump(items, file, indent=4)


def view_items(items):
    print("\n--- Store Inventory ---")
    print("ID | Item | Price | Quantity")
    for item in items:
        print(f'{item["id"]} | {item["name"]} | {item["price"]} | {item["quantity"]}')


def add_item(items):
    try:
        name = input("Item name: ")
        price = float(input("Item price: "))
        quantity = int(input("Quantity: "))
        item_id = max([item["id"] for item in items]) + 1

        items.append({
            "id": item_id,
            "name": name,
            "price": price,
            "quantity": quantity
        })
        save_items(items)
        print("Item added successfully.")
    except ValueError:
        print("Invalid input.")


def update_quantity(items):
    try:
        item_id = int(input("Enter item ID: "))
        for item in items:
            if item["id"] == item_id:
                qty = int(input("Enter new quantity: "))
                item["quantity"] = qty
                save_items(items)
                print("Quantity updated.")
                return
        print("Item not found.")
    except ValueError:
        print("Invalid input.")


def sell_item(items):
    try:
        item_id = int(input("Enter item ID: "))
        for item in items:
            if item["id"] == item_id:
                qty = int(input("Enter quantity to sell: "))
                if qty <= item["quantity"]:
                    item["quantity"] -= qty
                    save_items(items)
                    print("Sale successful.")
                else:
                    print("Not enough stock.")
                return
        print("Item not found.")
    except ValueError:
        print("Invalid input.")


def delete_item(items):
    try:
        item_id = int(input("Enter item ID to delete: "))
        for item in items:
            if item["id"] == item_id:
                items.remove(item)
                save_items(items)
                print("Item deleted.")
                return
        print("Item not found.")
    except ValueError:
        print("Invalid input.")


def main():
    items = load_items()

    while True:
        print("\n--- Store Menu ---")
        print("1. View Items")
        print("2. Add Item")
        print("3. Update Quantity")
        print("4. Sell Item")
        print("5. Delete Item")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            view_items(items)
        elif choice == "2":
            add_item(items)
        elif choice == "3":
            update_quantity(items)
        elif choice == "4":
            sell_item(items)
        elif choice == "5":
            delete_item(items)
        elif choice == "6":
            print("Exiting Store System.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
