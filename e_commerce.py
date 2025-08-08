# e_commerce.py

class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product.pid in self.items:
            self.items[product.pid]['quantity'] += quantity
        else:
            self.items[product.pid] = {'product': product, 'quantity': quantity}

    def remove_item(self, product):
        if product.pid in self.items:
            del self.items[product.pid]

    def view_cart(self):
        if not self.items:
            print("🛒 Your cart is empty.")
        else:
            print("\n🛍️ Items in Cart:")
            total = 0
            for item in self.items.values():
                p = item['product']
                q = item['quantity']
                print(f"{p.name} x {q} = ₹{p.price * q}")
                total += p.price * q
            print(f"Total: ₹{total}")

    def checkout(self):
        if not self.items:
            print("🛒 Your cart is empty. Add something first.")
        else:
            self.view_cart()
            print("✅ Checkout successful! Thank you for shopping.")
            self.items.clear()

# Sample product list
products = [
    Product(1, "Smartphone", 15000),
    Product(2, "Headphones", 2500),
    Product(3, "Laptop", 55000),
    Product(4, "Smartwatch", 2000),
    Product(5, "Bluetooth Speaker", 1000)
]

def show_products():
    print("\n🛍️ Available Products:")
    for p in products:
        print(f"{p.pid}. {p.name} - ₹{p.price}")

def find_product(pid):
    for p in products:
        if p.pid == pid:
            return p
    return None

def main():
    cart = Cart()

    while True:
        print("\n--- E-Commerce Menu ---")
        print("1. Show Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            show_products()
        elif choice == '2':
            show_products()
            try:
                pid = int(input("Enter Product ID to add: "))
                quantity = int(input("Enter quantity: "))
                product = find_product(pid)
                if product:
                    cart.add_item(product, quantity)
                    print(f"✅ Added {product.name} x{quantity} to cart.")
                else:
                    print("❌ Invalid Product ID.")
            except ValueError:
                print("❌ Please enter valid numbers.")
        elif choice == '3':
            try:
                pid = int(input("Enter Product ID to remove: "))
                product = find_product(pid)
                if product:
                    cart.remove_item(product)
                    print(f"🗑️ Removed {product.name} from cart.")
                else:
                    print("❌ Invalid Product ID.")
            except ValueError:
                print("❌ Invalid input.")
        elif choice == '4':
            cart.view_cart()
        elif choice == '5':
            cart.checkout()
        elif choice == '6':
            print("👋 Thank you for visiting!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
