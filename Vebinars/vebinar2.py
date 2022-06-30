""" a = "gjhgjgjhgjhg t5 79987jljlkjljlj"
b = [int(num) for num in a if num.isdigit()]
print(b) """

""" v = [abs(item) for item in range(-100,200) if item % 30 == 0 or item % 35 == 0]
print(v) """

""" ########### Finding dir in 
from pathlib import Path
import sys

p = Path(sys.argv[1]) # 1- means - 1 param in CMD

def parse_folder_recursion(path):
    for element in path.iterdir():
        if element.is_dir():
            print(f"This is folder - {element.name}")
            parse_folder_recursion(element)
        else:
            print(f"This is file - {element.name}")

if __name__ == "__main__":
    parse_folder_recursion(p) """


""" ###### Using Lambda function
from ast import operator


def if_elif_vs_dict(operator, x, y):
    return {
        "+": lambda: x + y,
        "-": lambda: x - y,
        "*": lambda: x * y,
        "/": lambda: x / y,
    }.get(operator, lambda: "This is not valid operation")()
    

print(if_elif_vs_dict ("+", 4, 5)) """



#### Coding Morse
morse_dict = { 
                    'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def convert_to_morse(text: str) -> str:
    result = []
    text = text.upper()
    for s in text:
        if s in morse_dict:
            result.append(morse_dict.get(s))
    return "|".join(result)

if __name__ == "__main__":
    text = input("please set text: ")
    result = convert_to_morse(text)
    print(result)
