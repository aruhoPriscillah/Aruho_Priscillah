# Simple Inventory Management System using Loops

inventory = {}

def display_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        print("-" * 30)
        for item, quantity in inventory.items():
            print(f"{item}: {quantity} in stock")
        print("-" * 30)

def add_item():
    item = input("Enter item name to add: ").strip().capitalize()
    if item in inventory:
        print("Item already exists. Use update option instead.")
    else:
        quantity = int(input(f"Enter quantity of '{item}': "))
        inventory[item] = quantity
        print(f"Added {item} with quantity {quantity}.")

def update_stock():
    item = input("Enter item name to update: ").strip().capitalize()
    if item in inventory:
        quantity = int(input(f"Enter new quantity for '{item}': "))
        inventory[item] = quantity
        print(f"Updated {item} to quantity {quantity}.")
    else:
        print("Item not found in inventory.")

def remove_item():
    item = input("Enter item name to remove: ").strip().capitalize()
    if item in inventory:
        del inventory[item]
        print(f"{item} removed from inventory.")
    else:
        print("Item not found.")

# Main loop
while True:
    print("\nInventory Management System")
    print("1. Display Inventory")
    print("2. Add Item")
    print("3. Update Stock")
    print("4. Remove Item")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        display_inventory()
    elif choice == '2':
        add_item()
    elif choice == '3':
        update_stock()
    elif choice == '4':
        remove_item()
    elif choice == '5':
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Please try again.")
