from product import Product
from inventory import Inventory
from user import USERS
inventory = Inventory()

def select_user():
    print("\n=== SELECT USER ===")
    print("1. USER1 (ADMIN)")
    print("2. USER2 (END USER)")

    choice = input("Choose user: ")

    user = USERS.get(choice)
    if not user:
        print("Invalid choice. Defaulting to USER2")
        user = USERS["2"]

    return user



def add_product_ui():
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    supplier = input("Enter Supplier: ")

    product = Product(product_id, name, category, price, quantity, supplier)
    inventory.add_product(product)
    print("✅ Product added successfully")

def search_menu():
    print("\n1. Search by ID")
    print("2. Search by Name")
    print("3. Search by Category")
    choice = input("Choose: ")

    if choice == "1":
        pid = input("Product ID: ")
        p = inventory.search_by_id(pid)
        print(p if p else "❌ Not found")

    elif choice == "2":
        name = input("Name: ")
        for p in inventory.search_by_name(name):
            print(p)

    elif choice == "3":
        cat = input("Category: ")
        for p in inventory.search_by_category(cat):
            print(p)

def filter_menu():
    print("\n1. Low Stock")
    print("2. Price Range")
    print("3. Category")
    choice = input("Choose: ")

    if choice == "1":
        results = inventory.filter_low_stock()
    elif choice == "2":
        min_p = float(input("Min price: "))
        max_p = float(input("Max price: "))
        results = inventory.filter_by_price_range(min_p, max_p)
    elif choice == "3":
        cat = input("Category: ")
        results = inventory.filter_by_category(cat)
    else:
        return

    for p in results:
        print(p)

def main_menu(user):
    while True:
        print(f"\n=== MENU ({user.role}) ===")
        if user.role == "ADMIN":
            print("1. Add Product")
            print("2. View All Products")
            print("3. Search Product")
            print("4. Filter Products")
            print("5. Exit")
        else:
            print("1. View All Products")
            print("2. Search Product")
            print("3. Filter Products")
            print("4. Exit")

        choice = input("Choose: ")

        if user.role == "ADMIN":
            if choice == "1":
                add_product_ui()
            elif choice == "2":
                inventory.view_all_products()
            elif choice == "3":
                search_menu()
            elif choice == "4":
                filter_menu()
            elif choice == "5":
                break
        else:
            if choice == "1":
                inventory.view_all_products()
            elif choice == "2":
                search_menu()
            elif choice == "3":
                filter_menu()
            elif choice == "4":
                break

if __name__ == "__main__":
    user = select_user()
    main_menu(user)
