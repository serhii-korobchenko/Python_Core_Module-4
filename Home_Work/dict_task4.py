""" Современная система оценок в университете имеет следующий вид:

Оценка	Баллы	Оценка ECTS	Объяснение
1	0-34	F	Unsatisfactorily
2	35-59	FX	Unsatisfactorily
3	60-66	E	Enough
3	67-74	D	Satisfactorily
4	75-89	C	Good
5	90-95	В	Very good
5	96-100	A	Perfectly
Реализуйте две функции. Первая будет использоваться в бухгалтерии 
при расчете стипендии, get_grade принимает ключ в оценке ECTS, 
и должна возвращать соответствующую пятибалльную оценку (первый столбик таблицы). 
Вторая get_description тоже принимает ключ в оценке ECTS, 
но будет возвращать объяснение оценки в текстовом формате (последний столбик таблицы) 
и будет использоваться в электронной зачетке студента. 
На несуществующий ключ функции 
должны возвращать значение None. """

def get_grade(key): 
    return estimation_dict_grade.get(key)
    
    
def get_description(key):
    return estimation_dict_discrip.get(key)

estimation_dict_grade = {
"F": 1,	
"FX": 2,
"E": 3,	
"D": 3,	
"C": 4,	
"B": 5,	
"A": 5
}

estimation_dict_discrip = {
"F": "Unsatisfactorily",
"FX": "Unsatisfactorily",
"E": "Enough",
"D": "Satisfactorily",
"C": "Good",
"B": "Very good",
"A": "Perfectly"
}

key_in = "B"
print(get_grade(key_in))
print(get_description(key_in))