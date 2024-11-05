class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount):
        '''Add stock for the product. '''
        self.quantity += amount
        print(f"Added {amount} units to {self.name}. Total stock: {self.quantity}.")

    def reduce_stock(self, amount):
        '''Remove stock from the product after a sale'''
        if self.quantity >=amount:
            self.quantity -= amount
            print(f"Sold {amount} units of {self.name}. Remaining stock: {self.quantity}")
            return True
        else:
            print(f"Not enough stock for {self.name}. Only {self.quantity} units available.")
            return False
        
class Inventory:
    def __init__(self):
        self.products = {} # Dictionary to store product details

    def add_product(self, product_id, name, price, quantity):
        '''Add a new product to the inventory.'''
        if product_id not  in self.products:
            product = Product(product_id, name, price, quantity)
            self.products[product_id] = product
            print(f"Product {name} added to inventory with {quantity} units.")
        else:
            print(f"Product with ID {product_id} already exits.")

    def restock_product(self, product_id, amount):
        '''Restock an existing product.'''
        if product_id in self.products:
            self.products[product_id].add_stock(amount)
        else:
            print(f"Product with ID {product_id} not found.")

    def sell_product(self, product_id, amount):
        '''Process a sale by reducing product stock.'''
        if product_id in self.products:
            success = self.products[product_id].reduce_stock(amount)
            if success:
                print(f"Sale processed for {amount} units of {self.products[product_id].name}.")
            else:
                print("Sale could not be completed use to unsufficient stock.")

        else:
            print(f"Product with ID {product_id} not found")
    
    def check_low_stock(self, threshold):
        '''List all products that are below the given stocks thresold'''
        low_stock_items = [product for product in self.products.values() if product.quantity < threshold ]
        if low_stock_items:
            print("Low stock items:")
            for product in low_stock_items:
                print(f"{product.name} - {product.quantity} units left (below {threshold}.)")
        else:
            print("No low stock itesms")

    def list_all_items(self):
        '''Display all products and their details.'''
        print("Inventory list :")
        for product in self.products.values():
            print(f"ID: {product.product_id}, Name: {product.name}, Price: ${product.price}, Quantity: {product.quantity}")


inventory = Inventory()

# Add products
inventory.add_product(101, "Apple", 0.50, 100)
inventory.add_product(102, "Banana", 0.30, 150)

# Restock a product
inventory.restock_product(101, 50)

# Sell some products
inventory.sell_product(101, 30)
inventory.sell_product(102, 10)

# Check for low stock items (threshold: 80 units)
inventory.check_low_stock(80)

# List all products in inventory
inventory.list_all_items()