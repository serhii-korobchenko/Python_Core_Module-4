""" # return value of element and delete pair: key-value
chars = {'a': 1, 'b': 2}
b_num = chars.pop('b')
print(chars)  # {'a': 1}
print(b_num)  # 2 """

#extend dict with value of another dict
""" chars = {'a': 1, 'b': 2}
chars.update({"c": 3})
print(chars)  # {'a': 1, 'b': 2, "c": 3} """

# clear dict
""" chars = {'a': 1, 'b': 2}
chars.clear()
print(chars)  # {} """
""" 
# return dict copy
chars = {'a': 1, 'b': 2}
chars_copy = chars.copy()
chars_copy == chars  # True """

""" # do not call exclution if dict does not contain key - return default, by default - default = None
chars = {'a': 1, 'b': 2}
c_idx = chars.get('c', -1)
print(c_idx)  # -1 """

""" # loop with dict
numbers = {
    1: "one",
    2: "two",
    3: "three"
}
for key in numbers.keys(): # with keys
    print(key)

for val in numbers.values(): # with values
    print(val)

for key, value in numbers.items(): # with pair: key + value
    print(key, value) """


""" # Using tuples as keys in dicts ----> ERROR?
points = {
    (0, 0): "O"
    (1, 1): "A"
    (2, 2): "B"
} """

