from pprint import pprint

def reader_recipes():
    with open('recipes.txt', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            line = line.strip()
            cook_book.update({line:[]})
            for ing in range(int(f.readline().strip())):
                lst = f.readline().strip().split('|')
                dict = {'ing_name':lst[0], 'quant':lst[1], 'measure':lst[2]}
                cook_book[line].append(dict)
            f.readline()    
        return cook_book         
                





def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for dish in dishes:
            for item in reader_recipes()[dish]:
                items_list = dict([(item['ing_name'], {'measure': item['measure'], 'quant': int(item['quant'])*person_count})])
                if shopping_list.get(item['ing_name']):
                    extra_item = (int(shopping_list[item['ing_name']]['quant']) +
                                  int(items_list[item['ing_name']]['quant']))
                    shopping_list[item['ing_name']]['quant'] = extra_item

                else:
                    shopping_list.update(items_list)
    return shopping_list
   
  


           
pprint(get_shop_list_by_dishes(['Омлет','Фахитос'], 10))            