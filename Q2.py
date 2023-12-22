class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, code, name, price):
        product = Product(code, name, price)
        self.products.append(product)

    def display_menu(self):
        print("Product Menu:")
        print("{:<10} {:<20} {:<10}".format("Code", "Name", "Price"))
        for product in self.products:
            print("{:<10} {:<20} {:<10}".format(product.code, product.name, product.price))

    def generate_bill(self, orders):
        total_price = 0
        print("\nGenerating Bill:")
        print("{:<20} {:<10} {:<10}".format("Product", "Quantity", "Price"))
        for code, quantity in orders.items():
            product = next((p for p in self.products if p.code == code), None)
            if product:
                item_price = product.price * quantity
                total_price += item_price
                print("{:<20} {:<10} {:<10}".format(product.name, quantity, item_price))
            else:
                print(f"Product with code {code} not found in the store.")
        print("\nTotal Price: {}".format(total_price))

# Example usage:
store = Store()

# Adding products to the store
store.add_product("P001", "Laptop", 1200)
store.add_product("P002", "Printer", 150)
store.add_product("P003", "Mouse", 20)

# Displaying the menu
store.display_menu()

# Generating a sample bill
order = {"P001": 2, "P002": 1}
store.generate_bill(order)
