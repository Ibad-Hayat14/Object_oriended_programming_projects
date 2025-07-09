import json

class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} - ID: {self.product_id}, Quantity: {self.quantity}, Price: ${self.price:.2f}"

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print(f"Product ID {product.product_id} already exists. Updating quantity.")
            self.products[product.product_id].quantity += product.quantity
        else:
            self.products[product.product_id] = product
        print(f"Product '{product.name}' added/updated in inventory.")

    def update_product(self, product_id, quantity=None, price=None):
        if product_id in self.products:
            if quantity is not None:
                self.products[product_id].quantity = quantity
            if price is not None:
                self.products[product_id].price = price
            print(f"Product ID {product_id} updated.")
        else:
            print(f"Product ID {product_id} not found.")

    def remove_product(self, product_id):
        if product_id in self.products:
            removed_product = self.products.pop(product_id)
            print(f"Product '{removed_product.name}' removed from inventory.")
        else:
            print(f"Product ID {product_id} not found.")

    def view_inventory(self):
        if self.products:
            print("Inventory:")
            for product in self.products.values():
                print(product)
        else:
            print("The inventory is empty.")

    def low_stock_report(self, threshold):
        print(f"Low stock products (threshold: {threshold}):")
        for product in self.products.values():
            if product.quantity < threshold:
                print(product)

    def save_to_file(self, filename):
        data = {
            pid: {"name": product.name, "quantity": product.quantity, "price": product.price}
            for pid, product in self.products.items()
        }
        with open(filename, "w") as file:
            json.dump(data, file)
        print(f"Inventory saved to {filename}.")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for pid, details in data.items():
                    self.products[pid] = Product(pid, details["name"], details["quantity"], details["price"])
            print(f"Inventory loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding data from {filename}.")

# Example Usage
if __name__ == "__main__":
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. View Inventory")
        print("5. Low Stock Report")
        print("6. Save Inventory to File")
        print("7. Load Inventory from File")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
            product = Product(product_id, name, quantity, price)
            inventory.add_product(product)

        elif choice == "2":
            product_id = input("Enter Product ID: ")
            quantity = input("Enter New Quantity (leave blank to skip): ")
            price = input("Enter New Price (leave blank to skip): ")
            quantity = int(quantity) if quantity else None
            price = float(price) if price else None
            inventory.update_product(product_id, quantity, price)

        elif choice == "3":
            product_id = input("Enter Product ID to Remove: ")
            inventory.remove_product(product_id)

        elif choice == "4":
            inventory.view_inventory()

        elif choice == "5":
            threshold = int(input("Enter Low Stock Threshold: "))
            inventory.low_stock_report(threshold)

        elif choice == "6":
            filename = input("Enter Filename to Save: ")
            inventory.save_to_file(filename)

        elif choice == "7":
            filename = input("Enter Filename to Load: ")
            inventory.load_from_file(filename)

        elif choice == "8":
            print("Exiting Inventory Management System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
