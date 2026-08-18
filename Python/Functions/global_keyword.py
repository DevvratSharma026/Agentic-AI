chai_type = 'Plain'

def update_order():
    global chai_type # use to modify the global variables 
    chai_type = 'Ginger'

update_order()
print(f'chai type is {chai_type}')
    