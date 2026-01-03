from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def view_all_products(self):
        if not self.products:
            print("No products available.")
            return
        for product in self.products:
            print(product)

    def search_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def search_by_name(self, name):
        return [p for p in self.products if name.lower() in p.name.lower()]

    def search_by_category(self, category):
        return [p for p in self.products if p.category.lower() == category.lower()]

    def filter_low_stock(self, threshold=5):
        return [p for p in self.products if p.quantity <= threshold]

    def filter_by_price_range(self, min_price, max_price):
        return [p for p in self.products if min_price <= p.price <= max_price]

    def filter_by_category(self, category):
        return self.search_by_category(category)
