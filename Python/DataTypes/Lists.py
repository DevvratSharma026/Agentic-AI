# Lists in python is a collection of items that are ordered and changeable. Lists are written with square brackets. It is a mutable data type, which means we can change the elements of a list after it has been created. Lists can contain elements of different data types, including other lists.
# Creating a list

my_list = ["apple", "banana", "cherry", ["kiwi", "mango"], 1, 3, True, False];

# insert(): inserting an element at any specific position
my_list.insert(4, "grapes")
print(my_list)

#append(): adding an element at the end of the list
my_list.append(["orange", "watermelon"])
print(my_list)

#extend(): adding multiple elements at the end of the list, extend is used to add elements from an iterable (like a list, tuple, or string) to the end of the list. It takes an iterable as an argument and adds each element of that iterable to the end of the list.
my_list.extend("kiwi"); # this will print like ['apple', 'banana', 'cherry', ['kiwi', 'mango'], 'grapes', ['orange', 'watermelon'], 'k', 'i', 'w', 'i']
print(my_list)

my_list.pop() # this will remove the last element from the list
my_list.copy() # this will create a shallow copy of the list
my_list.clear() # this will clear the list and make it empty
