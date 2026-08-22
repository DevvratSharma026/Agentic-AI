#Syntax: [ expression for item in iterable if condition ]

menu = [
    "masala chai",
    "iced lemin tea",
    "Green chai",
    "iced peach tea",
    "ginger tea"
]

iced_tea = [val for val in menu if len(val) > 10]

#step1: for val in menu: will loop through the whole list one by one
#step2: if len(val) > 10: checks the condition for each item
#step3: if any value found to be true it will get inserted in val which is at the very start of the expression

print(iced_tea)