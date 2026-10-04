# Q17: Shopping Cart using Functions
# Why functions? Each job (add, remove, view, total, checkout) is separate logic,
# so each gets its own function that is small, reusable and easy to test.
# Why a while loop? We don't know how many actions the user will take; the
# program runs until checkout or exit.
# Why for loops inside? view_cart and calculate_total visit every cart item.


def add_item(cart, name, price, quantity):
    """Add an item to the cart. If it already exists, increase its quantity.
    Returns the new quantity of that item."""
    if name in cart:
        cart[name]["qty"] += quantity
    else:
        cart[name] = {"price": price, "qty": quantity}
    return cart[name]["qty"]


def remove_item(cart, name):
    """Remove an item completely. Returns True if removed, False if not found."""
    if name in cart:
        del cart[name]
        return True
    return False


def calculate_total(cart):
    """Return the total cost of everything in the cart."""
    total = 0
    for name in cart:
        total += cart[name]["price"] * cart[name]["qty"]
    return total


def view_cart(cart):
    """Print every item with its subtotal, and the cart total."""
    if len(cart) == 0:
        print("Your cart is empty.")
        return

    print(f"\n{'Item':<15}{'Price':>10}{'Qty':>6}{'Subtotal':>12}")
    print("-" * 43)
    for name in cart:
        price = cart[name]["price"]
        qty = cart[name]["qty"]
        print(f"{name:<15}{price:>10.2f}{qty:>6}{price * qty:>12.2f}")
    print("-" * 43)
    print(f"{'Total':<31}{calculate_total(cart):>12.2f}")


def checkout(cart):
    """Print the final receipt. Returns True if checkout happened, False if cart is empty."""
    if len(cart) == 0:
        print("Your cart is empty. Add items before checking out.")
        return False

    print("\n===== RECEIPT =====")
    view_cart(cart)
    print(f"\nAmount to pay: ₹{calculate_total(cart):,.2f}")
    print("Thank you for shopping with us!")
    return True


def main():
    cart = {}
    print("Welcome to the Shopping Cart")

    while True:
        print("\n----- Menu -----")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Item name: ").strip().lower()
            if name == "":
                print("Item name cannot be empty.")
                continue
            try:
                price = float(input("Price per unit: ₹"))
                quantity = int(input("Quantity: "))
            except ValueError:
                print("Invalid input. Price must be a number and quantity a whole number.")
                continue
            if price <= 0 or quantity <= 0:
                print("Price and quantity must be greater than zero.")
                continue

            new_qty = add_item(cart, name, price, quantity)
            print(f"Added. You now have {new_qty} x {name} in the cart.")

        elif choice == "2":
            name = input("Item name to remove: ").strip().lower()
            if remove_item(cart, name):
                print(f"'{name}' removed from the cart.")
            else:
                print(f"'{name}' is not in the cart.")

        elif choice == "3":
            view_cart(cart)

        elif choice == "4":
            if checkout(cart):
                break                      # successful checkout ends the program

        elif choice == "5":
            print("Exiting without checkout. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()