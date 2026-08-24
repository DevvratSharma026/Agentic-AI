#namespace: each object has it's own entity, properties called as 'namespace'
class Chai:
    origin = "India"
    
print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

#creating objects from class Chai
masala = Chai()

masala.is_hot = False
print(f"From class {Chai.is_hot}") #output: true
print(f"from object {masala.is_hot}") #output: false, this show that each object has it's namespace and do not affect other objects and class

masala.flavour = 'masala'
print(masala.flavour)
print(Chai.flavour) #error here, any new property we make in object will not be in the class