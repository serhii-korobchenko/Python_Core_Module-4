""" Есть четырехугольная схема полетов дрона с координатами (1, 2, 3, 4). 
У нас есть словарь points, ключи которого — кортежи, точки полета между координатами 
четырехугольника, вида (1, 2). Значения словаря — это расстояния между указанными точками.

points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7, (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}
Напишите функцию calculate_distance, которая на вход принимает список координат 
четырехугольника из словаря вида [0, 1, 3, 2, 0]. Функция должна подсчитать, 
используя указанный словарь, какое общее расстояние пролетит дрон, двигаясь между точками.

Примечания:

при взятии у словаря points значения, в ключ-кортеже всегда должна быть первой 
координата с меньшим значением — (2, 3), но не (3, 2);
для пустого списка и списка с одной координатой функция calculate_distance должна возвращать 0. """


points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    distance = 0
    for i in range(len(coordinates)-1):
        first_val = coordinates[i]
        second_val = coordinates[i+1]
        if first_val > second_val:
            first_val, second_val = second_val, first_val
        tup = tuple ([first_val, second_val])
        #print(first_val, second_val)
        #print (tup)

        for key, value in points.items():
            if key == tup:
                distance += value

    print (distance)
    return distance

#calculate_distance([0, 1, 3, 2, 0])
#calculate_distance([])
calculate_distance([0, 1, 3, 2, 0, 2]) # 17.6