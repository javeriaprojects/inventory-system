import json
import csv
import os
from typing import List

class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name} - ${self.price} x {self.quantity}"

    def total_price(self) -> float:
        return self.price * self.quantity

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

class Inventory:
    def __init__(self):
        self.items: List[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, name: str) -> None:
        self.items = [i for i in self.items if i.name != name]

    def calculate_total_value(self) -> float:
        return sum(item.total_price() for item in self.items)

    def show_inventory(self) -> None:
        print("\n📦 Current Inventory:")
        for item in self.items:
            print("•", item)

    def export_json(self, filename: str = "inventory.json") -> None:
        data = [item.to_dict() for item in self.items]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"✅ Exported to {os.path.abspath(filename)}")

    def export_csv(self, filename: str = "inventory.csv") -> None:
        with open(filename, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["name", "price", "quantity"])
            writer.writeheader()
            for item in self.items:
                writer.writerow(item.to_dict())
        print(f"✅ Exported to {os.path.abspath(filename)}")

def run_inventory_app():
    store = Inventory()
    print("📋 Welcome to the Inventory System!")
    print(f"🖥️ Running on: {os.name.upper()} ({os.getcwd()})")

    while True:
        print("\nChoose an action:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Show inventory")
        print("4. Export to JSON")
        print("5. Export to CSV")
        print("6. Calculate total value")
        print("0. Exit")

        choice = input("Enter option: ")

        if choice == "1":
            name = input("Item name: ")
            try:
                price = float(input("Item price: "))
                quantity = int(input("Quantity: "))
                store.add_item(Item(name, price, quantity))
                print("✅ Item added.")
            except ValueError:
                print("⚠️ Invalid input. Please enter numeric price and quantity.")

        elif choice == "2":
            name = input("Enter item name to remove: ")
            store.remove_item(name)
            print("🗑️ Item removed.")

        elif choice == "3":
            store.show_inventory()

        elif choice == "4":
            store.export_json()

        elif choice == "5":
            store.export_csv()

        elif choice == "6":
            total = store.calculate_total_value()
            print(f"💰 Total inventory value: ${total:.2f}")

        elif choice == "0":
            print("👋 Exiting Inventory System.")
            break

        else:
            print("❌ Invalid option, try again.")

# 🧪 Uncomment below to run locally
# run_inventory_app()

    