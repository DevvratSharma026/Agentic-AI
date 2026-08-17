# enumerate() is used to iterate over an iterable while keeping track of the index of each element.

menu = ['green', 'lemon', 'spiced', 'mint']

for idx, item in enumerate(menu, start= 0):
    print(idx, item) 