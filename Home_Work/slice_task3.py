""" Мы разрабатываем кулинарный блог. И в рецептах, при написании списка ингредиентов, 
мы разделяем их запятыми, а перед последним ставим союз "and", как в примере ниже:

2 eggs, 1 liter sugar, 1 tsp salt and vinegar

Напишите функцию format_ingredients, которая будет принимать на вход список из ингредиентов 
["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] и возвращать собранную строку 
из его элементов в описанный выше способ. Ваша функция должна уметь 
обрабатывать списки любой длины """

def format_ingredients(items):
    result = ""
    if len(items) == 1:
        result += items[-1]
    else:
        for value in items:
            result += value
            if value == items [-2]:
                result += " and "
            elif value == items [-1]:
                result = result
            else:
                result += ", "
    return result


print(format_ingredients(["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]))
print(format_ingredients(["2 eggs"]))