# Tuples: Ordered, immutable collections in Python
my_tuple = ("chole bhature", "pav bhaji", "rajma chawal")

# this is know as unpacking of the tuple, where we assign the values of the tuple to individual variables, and to do this we should be knowing the exact number of elements in the tuple, otherwise it will throw an error.
(food1, food2, food3) = my_tuple

print(f"my food is {food1}, {food2}, and {food3}")

# membership in tuple: we can check if an element is present in the tuple or not using the 'in' keyword. it is really case sensitive, so we should be careful while checking for membership in a tuple.
print(f"Is 'pav bhaji' present in my_tuple? {'pav bhaji' in my_tuple}")