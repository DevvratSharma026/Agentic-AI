#Attribute shadowing: if we update a attribute in object and delete it afterwards it will fallback to the original value of that is in the class, but if the attribute is new/we have made the attribute outside the class then there is an error cause ther is not fallback
class Chai:
    temp = "hot"
    strength = "strong"
    
cutting = Chai()
print("before change", cutting.temp)

cutting.temp = "mild"
cutting.cup = "small"
print("after change", cutting.temp)
print("direct look in class", Chai.temp)

del cutting.cup
print("after del", cutting.cup)