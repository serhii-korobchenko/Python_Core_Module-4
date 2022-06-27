""" # List example with forward recall
some_iterable = ["a", "b", "c"]
first_letter = some_iterable[0]
middle_one = some_iterable[1]
last_letter = some_iterable[2]

# List example with backward recall
some_iterable = ["a", "b", "c"]
first_letter = some_iterable[-3]
middle_one = some_iterable[-2]
last_letter = some_iterable[-1]

# Slice example
some_str = "This is awesome string"
first_five = some_str[0:5]

### 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[0:10:2]
even_numbers = numbers[1:10:2]
three_numbers = numbers[2:10:3]

###
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2:10:3]

numbers_copy = numbers[:] """
""" 
# Objects Using
numbers = ['a', 'b']
numbers.append('c')
print(numbers)  # ['a', 'b', 'c'] """

""" # Return i element and remove itfrom list
chars = ['a', 'b']
last = chars.pop(1)
print(chars)  # ['a']
print(last)  # 'b' """

""" # Extend list
chars = ['a', 'b']
numbers = [1, 2]
chars.extend(numbers)
print(chars)  # ['a', 'b', 1, 2]

#insert x on spesific position
chars = ["a", "b"]
chars.insert(1, "c")
print(chars)  # ['a', 'c', 'b'] """

""" # Clear list
chars = ['a', 'b']
last =  chars.clear() 
print(chars) # [] """

""" # Find index first element in list
chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c') 
print(c_ind) #2 """

""" # Return number of elements in list equel x
chars = ['a', 'b', 'c', 'a']
a_count = chars.count('c')
print(a_count) # 2 """

""" # Sort sort ascending list 
chars = ['z', 'a', 'b']
chars.sort()
print(chars) # ['a', 'b', 'z'] """

""" # Change order of elements in list on opposite
chars = ['a', 'b']
chars.reverse()
print(chars) # ['b', 'a'] """

""" # return copy of list
chars =  ['a', 'b']
chars_copy = chars.copy()
chars == chars_copy # True """






