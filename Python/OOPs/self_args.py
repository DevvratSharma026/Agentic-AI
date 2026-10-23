class Chaicup:
    size = 120
    
    # 'self' represents the specific instance of the class that is calling the method.
    # It acts as a reference/pointer to access instance variables and methods.
    def describe(self):
        # Accesses 'size' relative to the specific instance calling 'describe()'
        return f"A {self.size}ml cup chai."
    

# --- INSTANTIATION ---
cup = Chaicup()


# --- METHOD CALL METHOD 1: Instance Syntax (Syntactic Sugar) ---

# Python automatically passes 'cup' as the first argument ('self') under the hood!
# Execution: cup.describe() ---> Chaicup.describe(cup)
print(cup.describe())  # Output: A 120ml cup chai.


# --- METHOD CALL METHOD 2: Direct Class Call (Under the Hood) ---

# When calling a method directly via the Class name ('Chaicup'), Python DOES NOT 
# automatically bind an instance. You MUST manually pass the instance reference ('cup') 
# into the 'self' parameter.
print(Chaicup.describe(cup))  # Output: A 120ml cup chai.