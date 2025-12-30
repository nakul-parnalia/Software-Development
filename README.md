#  Store Inventory Management System 

##  Scenario

A small store sells **7 different items**, each with:

* Item ID
* Item Name
* Price
* Quantity

Users can:

1. View items
2. Add new items
3. Update quantity
4. Sell items (reduce quantity)
5. Delete items
6. Save data persistently

---

# 1 Data Structure Used

```python
items = [
    {"id": 1, "name": "Rice", "price": 50, "quantity": 20}
]
```

---

# 2 Default Store Items 

| ID | Item Name | Price | Quantity |
| -- | --------- | ----- | -------- |
| 1  | Rice      | 50    | 20       |
| 2  | Sugar     | 40    | 15       |
| 3  | Oil       | 120   | 10       |
| 4  | Milk      | 30    | 25       |
| 5  | Bread     | 25    | 18       |
| 6  | Eggs      | 6     | 50       |
| 7  | Soap      | 35    | 30       |


# 3 Error Handling Implemented

 Invalid numeric input
 Selling more than stock
 Missing item ID
 Corrupted file handling

---

# 4 Flowchart

```
Start
  ↓
Load Items
  ↓
Display Menu
  ↓
View / Add / Update / Sell / Delete
  ↓
Save Changes
  ↓
Exit
```

---

# 5 Waterfall Model 

1. Requirement Analysis – Store inventory needs
2. System Design – Menu, data structure
3. Implementation – Python coding
4. Testing – Input validation
5. Deployment – CLI usage
6. Maintenance – Add billing / reports

---

# 6 Week Planning Chart

| Week | Work                   |
| ---- | ---------------------- |
| 1    | Store problem analysis |
| 2    | Inventory data design  |
| 3    | Flowchart & logic      |
| 4    | Core coding            |
| 5    | File storage           |
| 6    | Error handling         |
| 7    | Testing                |
| 8    | Documentation          |
| 9    | Final submission       |

---

# 7 Store Inventory Management System

## Description
The Store Inventory Management System is a Python-based application designed to manage the inventory of a small retail store. 
The system comes with seven default items, each defined by an item ID, name, price, and available quantity. 
It allows users to efficiently track and manage stock through a simple and interactive command-line interface.

This project demonstrates fundamental programming concepts such as data structures, 
file handling, 
user interaction, 
error handling,  
modular program design. 
It is suitable for academic assessment and as an introductory portfolio project.

---

## Run Instructions
Follow the steps below to run the application:

1. Ensure Python 3 is installed on your system.
2. Save the program file as `store_inventory.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the file.

## python store_inventory.py
The application will display a menu that allows the user to interact with the store inventory.

## Data Storage
The system uses a JSON file named store_items.json to store inventory data persistently.
The file contains item details such as ID, name, price, and quantity.
If the file does not exist, the system automatically initializes the inventory with seven default items.
All updates made during program execution are saved automatically to the file.
This ensures that inventory data is preserved even after the application is closed.

## Features
All inventory data is saved using file handling techniques, ensuring that item information is retained between program runs.

## Error Handling
The system includes proper error handling to manage invalid user input and unexpected situations, such as:
Invalid numeric input for price or quantity
Incorrect item ID selection
Attempting to sell more items than are available in stock
Missing or corrupted data files
Clear and meaningful error messages are provided to guide the user.

## Simple Command-Line Interface
The application uses a menu-driven command-line interface that is easy to understand and operate.
Each option is clearly labeled, allowing users to perform tasks such as
viewing items, adding new products, updating quantities, selling items, and deleting items.

## Educational Value
This project helps reinforce key programming concepts including:
Use of lists and dictionaries
File input/output using JSON
Modular programming with functions
Input validation and error handling
Real-world problem solving using Python


```




