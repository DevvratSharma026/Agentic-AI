# ==========================================
# 1. BASE CLASS (Parent Class)
# ==========================================

class BaseChai:
    def __init__(self, type_):
        # 'type_' uses an underscore to avoid shadowing Python's built-in 'type' keyword
        self.type = type_
        
    def prepare(self):
        print(f"Preparing {self.type} chai...")
        

# ==========================================
# 2. INHERITANCE ("IS-A" Relationship)
# ==========================================

# MasalaChai IS-A BaseChai.
# Passing BaseChai in parentheses allows MasalaChai to inherit all attributes 
# and methods (__init__, prepare) from BaseChai while adding its own new methods.
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, dry ginger")
        

# ==========================================
# 3. COMPOSITION ("HAS-A" Relationship)
# ==========================================

class ChaiShop:
    # Class-level attribute referencing the class object itself (not an instance).
    # This design pattern allows subclasses to swap out the factory class easily!
    chai_cls = BaseChai
    
    def __init__(self):
        # COMPOSITION IN ACTION:
        # ChaiShop HAS-A Chai object stored inside 'self.chai'.
        # Instantiates the class referenced in 'self.chai_cls' with argument 'Regular'.
        self.chai = self.chai_cls('Regular')
    
    def server(self):
        # Delegates tasks directly to the internal 'self.chai' object instance
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()
        

# ==========================================
# 4. POLYMORPHIC FACTORY OVERRIDE
# ==========================================

class FancyChaiShop(ChaiShop):
    # Overrides class attribute 'chai_cls' to point to 'MasalaChai' instead of 'BaseChai'.
    # When __init__ runs on FancyChaiShop, 'self.chai' becomes an instance of MasalaChai!
    chai_cls = MasalaChai


# ==========================================
# EXECUTION & OUTPUT TRACE
# ==========================================

shop = ChaiShop()        # Creates ChaiShop holding an instance of BaseChai('Regular')
fancy = FancyChaiShop()  # Creates FancyChaiShop holding an instance of MasalaChai('Regular')

print("--- Standard Shop ---")
shop.server()
# Output:
# Serving Regular chai in the shop
# Preparing Regular chai...

print("\n--- Fancy Shop ---")
fancy.server()
# Output:
# Serving Regular chai in the shop
# Preparing Regular chai...

print("\n--- Subclass Specific Method Call ---")
# Accesses the internal composed 'MasalaChai' instance and calls its specific method
fancy.chai.add_spices()
# Output:
# Adding cardamom, ginger, dry ginger