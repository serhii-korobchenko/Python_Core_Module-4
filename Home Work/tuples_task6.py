""" У нас есть список показателей студентов группы — это список с 
полученными балами по тестированию. Необходимо список поделить на две части. 
Напишите функцию split_list, которая принимает список (целые числа), 
находит среднее значение балла в списке и делит его на два списка. 
В первый попадают значения меньше среднего, включая среднее значение, 
а во второй — строго больше среднего. Функция возвращает кортеж этих двух списков. 
Для пустого списка возвращаем два пустых списка. """

def split_list(grade):
    try:

        averege_value = 0 #Calculation of avarage value
        sum_grade = 0
        less_list =[]
        more_list = []
        for item in grade:
            sum_grade += item
        averege_value =  sum_grade/len(grade)

        for item in grade:
            if item <= averege_value:
                less_list.append(item)
            else:
                more_list. append(item)

        joint_list = [less_list, more_list]
        t1 = tuple(joint_list)
        print(t1)
        return t1

    except ZeroDivisionError:
        less_list =[]
        more_list = []
        joint_list = [less_list, more_list]
        t1 = tuple(joint_list)
        print(t1)
        return t1
    

split_list([13, 15, 20, 45, 33, 28, 11, 17])
split_list([])

