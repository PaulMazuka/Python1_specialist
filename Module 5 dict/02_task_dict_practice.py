# Информация о товарах
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]

# 1. Выведите нумерованный список именований всех товаров
for num, item in enumerate(items, 1):
    print(f"{num}. {item['name']}")
lower_price = float(items[0]["price"])
# 2. Выведите цену самого дешевого товара
for item in items:
    if float(item["price"]) < lower_price:
        lower_price = float(item["price"])
print(lower_price)
