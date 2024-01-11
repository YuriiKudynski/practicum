class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Shop Name: {self.shop_name}")
        print(f"Store Type: {self.store_type}")

    def open_shop(self):
        print(f"{self.shop_name} is open")

    def display_number_of_units(self):
        print(f"Number of Units: {self.number_of_units}")

    def set_number_of_units(self, new_number):
        self.number_of_units = new_number

    def increment_number_of_units(self, increment_number):
        self.number_of_units += increment_number


class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = []

    def get_discount_products(self):
        print(f"Discounted products at {self.shop_name}: {self.discount_products}")