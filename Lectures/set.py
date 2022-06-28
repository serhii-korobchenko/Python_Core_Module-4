""" # Create set
a = set() # empty
a = set('hello') # filled
b = {1, 2, 3, 4} # another option --> not repeat the same element!!!
print(a)    # set()
print (b) """

""" # add element to set
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)    # {1, 2, 3, 4} """

""" # remove element
numbers = {1, 2, 3}
numbers.remove(3)
print(numbers)    # {1, 2} """

""" #remove element without calling extantion if it does not exist
numbers = {1, 2, 3}
numbers.discard(2)
print(numbers)    # {1, 3} """

# Operations with sets
a = set('hello')
b = set('hi there!')
print(f"a={a}") 
print(f"b={b}") 
print (f"a & b = {a & b}") # Finding of mutial elements in two sets
print (f"a ^ b = {a ^ b}") # Finding of all elements excluding mutial elements in two sets
print (f"a | b = {a | b}") # Uniting elements in two sets


