""" Создайте функцию parse_args, которая возвращает строку, 
составленную из аргументов командной строки, разделенных пробелами. 
Например, если скрипт был вызван командой: 

python run.py first second, 
то функция parse_args должна вернуть строку следующего вида 

"first second". """

import sys

def parse_args():
    result = ""
    result_list = []
    count = 0
    print (len(sys.argv))
    for arg in sys.argv:
        count +=1
        #print ("*")
        print(arg)
        if count >=2:
            result_list.append(arg)
    result =  " ".join([str(item) for item in result_list])   # Comprehention list
    
    return result

print(parse_args())

#Insert in terminal: python argv_task14.py first second
