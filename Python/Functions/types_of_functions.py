# Types of Functions
    # pure vs impure functions
    # Recursive Functions
    # Anonymous / Lambda Functions

#just work with themselves
def pure_chai(cups):
    return cups*10

total_chai = 0

#not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups
    
#recursive functions
def table(n):
    if n == 1:
        print(n)
        return n
    print(n)
    return table(n-1)

table(10)

#lambda: a function without name
square_lambda = lambda x: x*x
print(square_lambda(5))

add = lambda a, b: a+b
print(add(4, 5))

#lambda on list
elements = ["sodium", "gold", "silver", "titanium", "gold"]

gold_ele = list(filter(lambda gold: gold == "gold", elements))
print(gold_ele)