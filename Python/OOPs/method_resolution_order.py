# ==========================================
# METHOD RESOLUTION ORDER (MRO) - DIAMOND PROBLEM
# ==========================================

# Base ancestor class at the top of the diamond
class A:
    label = "A: Base class"
    
# Left branch inheriting from A
class B(A):
    label = "B: Masala blend"
    
# Right branch inheriting from A
class C(A):
    label = "C: Herbal blend"
    

# Multiple Inheritance: D inherits from both C and B.
# The order inside parentheses (C, B) defines the initial search priority!
class D(C, B):
    pass


# --- INSTANTIATION & ATTRIBUTE LOOKUP ---

cup = D()

# Python searches for 'label' following D's MRO sequence:
# 1. Look in D -> Not found.
# 2. Look in C (first specified parent) -> Found! label = "C: Herbal blend"
# 3. Stops immediately once found (B and A are never reached for this lookup).
print(cup.label)  # Output: C: Herbal blend

# Displays the exact MRO tuple representing the search path Python follows.
print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)