def chai_flavour():
    """chai flavour"""
    return "kadak"

#print the doc string at the every top of the function with """string""", it has to be at the very top of the function.
print(chai_flavour, __doc__) 

#__name__ shows the name of the function
print(chai_flavour, chai_flavour.__name__)

def generate_bill(chai = 0, samosa = 0):
    """
    calcualte bill:
    :param chai: number of chai cups (10 rupee)
    :param samsoa: number of samosa (15 rupee)
    total is: 
    """
    return (chai*10) + (samosa*15)

print(generate_bill, generate_bill.__doc__)
print(generate_bill(20, 20))
    