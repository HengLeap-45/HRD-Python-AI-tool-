# Coffee Shop Ordering Program

menu = [
    {"name": "Coffee", "price": 9.50},
    {"name": "Tea", "price": 5.00},
    {"name": "Latte", "price": 3.50},
    {"name": "Sandwich", "price": 5.00},
    {"name": "Cake", "price": 7.00},
]
cart = []


def show_menu():
    print("\n--- MENU ---")
    for i, item in enumerate(menu, 1):
        print(f"{i}. {item['name']} - ${item['price']:.2f}")


while True:
    print("\n1. View Menu")
    print("2. Add Item to Cart")
    print("3. Remove Last Item")
    print("4. View Cart & Total")
    print("5. Update Menu")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        show_menu()

    elif choice == "2":
        show_menu()
        num = int(input("Item number to add: "))
        if 1 <= num <= len(menu):
            cart.append(menu[num - 1])
            print(menu[num - 1]["name"], "added to cart.")
        else:
            print("Invalid item number.")

    elif choice == "3":
        if cart:
            removed = cart.pop()
            print(removed["name"], "removed from cart.")
        else:
            print("Your cart is empty.")

    elif choice == "4":
        print("\n--- YOUR CART ---")
        total = 0
        for item in cart:
            print(f"{item['name']} - ${item['price']:.2f}")
            total += item["price"]
        print("Items:", len(cart))
        print(f"Total: ${total:.2f}")

    elif choice == "5":
        print("\n1. Add new item")
        print("2. Change item price")
        sub = input("Choose (1-2): ")

        if sub == "1":
            name = input("New item name: ")
            price = float(input("New item price: "))
            menu.append({"name": name, "price": price})
            print(name, "added to menu.")

        elif sub == "2":
            show_menu()
            num = int(input("Item number to change: "))
            if 1 <= num <= len(menu):
                menu[num - 1]["price"] = float(input("New price: "))
                print("Price updated.")
            else:
                print("Invalid item number.")

        else:
            print("Invalid choice.")

    elif choice == "6":
        total = 0
        for item in cart:
            total += item["price"]
        print("\nFinal number of items:", len(cart))
        print(f"Final bill: ${total:.2f}")
        print("Thank you for visiting our coffee shop!")
        break

    else:
        print("Please choose 1 to 6.")