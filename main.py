print("Zadanie 1")
print("Lista zakupów")
shopping_dict = {
    "piekarnia" : ["chleb", "bułki", "pączek"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}
for shop, products in shopping_dict.items():
    products = [product.capitalize () for product in products]
    print(f"Idę do {shop.capitalize()} i kupuję tam: {products}.")
total = sum(len(products) for products in shopping_dict.values())
print("W sumie kupuję", total, "produktów.")
print("'Hiszpańska inkwizycja' to najlepszy skecz grupy Monty Pythona")
print("Nie jest to temat adekwatny do tego zadania")
print("Może i nie jest, ale to prawda")
