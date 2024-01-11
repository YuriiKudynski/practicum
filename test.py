from main import Shop, Discount

# Створення екземпляру класу Shop
store = Shop("MyStore", "General Store")

# Виведення атрибутів окремо
print(f"Shop Name: {store.shop_name}")
print(f"Store Type: {store.store_type}")
print()

# Виклик методів
store.describe_shop()
store.open_shop()
print()

# Зміна та виведення значення number_of_units
store.display_number_of_units()
store.number_of_units = 50
store.display_number_of_units()
print()

# Зміна та виведення значення number_of_units за допомогою методів
store.set_number_of_units(120)
store.display_number_of_units()
store.increment_number_of_units(30)
store.display_number_of_units()
print()

# Створення екземпляру класу Discount
store_discount = Discount("DiscountMart", "Discount Store")

# Додавання товарів зі знижкою до списку
store_discount.discount_products = ["Laptop", "Smartphone", "Headphones"]

# Виклик методу для виведення списку товарів зі знижкою
store_discount.get_discount_products()