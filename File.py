book_cook = {}
item_recipe = {}
ingredients_for_cook = []

with open("recipes.txt", "r", encoding="utf-8") as file:
    for line in file:
        recipe = line.strip()
        book_cook[recipe] = ' '
        quantity_ingredients = int(file.readline().strip())
        item_cook = ['ingredient_name', 'quantity', 'measure']
        for ingredients in range(quantity_ingredients):
            item_recipe = dict(zip(item_cook, file.readline().strip().split(" | ")))
            ingredients_for_cook.append(item_recipe)
            item_recipe = {}
        book_cook[recipe] = ingredients_for_cook
        ingredients_for_cook = []
        file.readline()
        print()


print(f'cook_book =  {book_cook}')


def get_shop_list_by_dishes(dishes, person_count):
    products_list = []
    for dish in dishes:
        i = 0
        while i < len(book_cook[dish]):
            products_list.append(book_cook[dish][i])
            i += 1

    print()
    all_products = {}
    products = {}

    for product in products_list:
        name = product['ingredient_name']
        if name in all_products.keys():
            products[name] += 1
        else:
            products[name] = 1
            all_products[name] = product

    print()

    for ingredient, product in all_products.items():
        del product['ingredient_name']
        product['quantity'] = int(product['quantity']) * int(products[ingredient]) * person_count

        return all_products


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
