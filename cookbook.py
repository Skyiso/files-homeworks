import json

with open('recipes.txt', 'rt', encoding='utf8') as rec_file:
    cook_book = {}
    for dishes_name in rec_file:
        ingredients_count = int(rec_file.readline())
        ingredients_list = []
        for i in range(ingredients_count):
            product, quantity, unit = rec_file.readline().strip().split(' | ')
            ingredients_list.append({
                'ingredient_name': product,
                'quantity': quantity,
                'measure': unit
            })
        rec_file.readline()
        cook_book[dishes_name.strip()] = ingredients_list
    res = json.dumps(cook_book, indent=2, ensure_ascii=False)
    print(f'cook_book = {res}')

