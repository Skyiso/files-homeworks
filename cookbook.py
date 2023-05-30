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

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                if ingredients['ingredient_name'] in result:
                    result[ingredients['ingredient_name']]['quantity'] += int(ingredients['quantity']) * person_count
                else:
                    result[ingredients['ingredient_name']] = {
                        'quantity': int(ingredients['quantity']) * person_count,
                        'measure': ingredients['measure']
                    }
        else:
            print('Блюдо не найдено')
    res = json.dumps(result, indent=2, ensure_ascii=False)
    print(f'\nДля приготовления блюд: {", ".join(dishes)} \nНа количество человек: {person_count} \nПотребуется: {res}')

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
get_shop_list_by_dishes(['Запеченный картофель', 'Картофельная запеканка'], 2)
get_shop_list_by_dishes(['Омлет', 'Сырники'], 4)