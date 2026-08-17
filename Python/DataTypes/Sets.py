# Sets in python are unordered collections of unique elements. They are mutable, meaning you can add or remove elements after the set has been created. Sets are defined using curly braces {} or the set() constructor.

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# union(): combining two sets to create a new set containing all unique elements from both sets
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# intersection(): finding common elements between two sets
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Spices only in essential: {only_in_essential}")

print(f"Is 'cloves' in essential_spices? {'cloves' in essential_spices}")

# frozenset(): creating an immutable set that cannot be modified after creation
immutable_spices = frozenset(essential_spices)