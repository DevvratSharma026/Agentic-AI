class Tealeaf:
    def __init__(self, age):
        # properties with _ in starting are special, they shouldn't be allowed to touch or change directly
        self._age = age
        
        
    #getter
    @property
    def age(self):
        return self._age + 2
    
    #setter
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea age must be between 1 and 5 years")
        
leaf = Tealeaf(2)
print(leaf.age)