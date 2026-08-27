#classmethod

class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
        
    @classmethod
    #cls -> taking whole class reference
    def from_dict(cls, order_detail):
        return cls(
            order_detail["tea_type"],
            order_detail["sweetness"],
            order_detail["size"]
        )
        
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split(",")
        return cls(tea_type, sweetness, size)
    
order1 = ChaiOrder.from_dict({
    "tea_type": "Masala chai",
    "sweetness": "Medium",
    "size": "small"
})

order2 = ChaiOrder.from_string("Ginger,low,medium")

print("--Order1--")
print(order1.__dict__)

print("--Order2--")
print(order2.__dict__)