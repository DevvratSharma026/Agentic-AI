#__init__
class OrderChai:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size
        
    def summary(self):
        return f"{self.size}ml of {self.type} cha i"
    
order = OrderChai("masala", 200)
print(order.summary())