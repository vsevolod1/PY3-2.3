#Делаем загрузку таблицы из файла
def cook_book():
    cook_book = {}
    with open('recipes.txt', 'r') as f:
        file_end = False
        while file_end == False:
            recipe = f.readline().strip()
            num = int(f.readline().strip())
            ingridient_list = []

            for _ in range(num):
                ingridients = f.readline().strip()
                ingridients = ingridients.split(' | ')
                ingridient_list.append({'ingridient_name': ingridients[0], 'quantity': int(ingridients[1]), 'measure': ingridients[2]})
                num -= 1

            cook_book[recipe] = ingridient_list
            if f.readline():
                file_end = False
            else:
                file_end = True
    return (cook_book)

#Формирование списка покупок
def get_shop_list_by_dishes(dishes, recipes_book, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in recipes_book[dish]:
      new_shop_list_item = dict(ingridient)
      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

#Вывод списка покупок
def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))


person_count = int(input('Введите количество человек: '))
dishes = input('Введите блюда в расчете на одного человека (через запятую): ').split(', ')
shop_list = get_shop_list_by_dishes(dishes, cook_book(), person_count)
print_shop_list(shop_list)
