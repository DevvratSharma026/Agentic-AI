# ==========================================
# 1. CODE DUPLICATION (Anti-Pattern)
# ==========================================

class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength
    
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # ❌ ANTI-PATTERN: Re-implementing parent logic manually
        # If Chai.__init__ changes in the future, GingerChai breaks or becomes inconsistent.
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level
        

# ==========================================
# 2. EXPLICIT CLASS CALL (Hardcoded)
# ==========================================

# ⚠️ BUG FIX NOTE: Added '(Chai)' inheritance so MasalaChai properly inherits from Chai.
class MasalaChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # Explicitly calling Chai.__init__ and manually passing 'self'.
        # Works fine for simple single inheritance, but creates hardcoded class dependencies 
        # and breaks easily in complex Multiple Inheritance hierarchies.
        Chai.__init__(self, type_, strength)
        self.spice_level = spice_level
        
    
# ==========================================
# 3. USING super() (Best Practice)
# ==========================================

class LemonChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # ✅ BEST PRACTICE: Uses Python's super() proxy object.
        # 1. Automatically passes 'self' implicitly under the hood (do NOT pass self!).
        # 2. Dynamically calculates the correct parent class using MRO (Method Resolution Order).
        super().__init__(type_, strength)
        self.spice_level = spice_level