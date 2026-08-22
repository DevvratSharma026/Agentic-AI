#Syntax:  { expression for item in iterable if condition } 
fav_chai = {
    "ginger chai",
    "green tea",
    "masala chai", 
    "ginger chai", 
    "lemon tea",
    "green tea",
    "ginger chai"
}

unique_chai = { ele for ele in fav_chai if len(ele) > 10}
print(unique_chai)

recipes = {
    "masala chai": ["ginger", "cardamom", "clove"],
    "elaichi chai": ["cardamom", "milk"],
    "spicy chai": ["ginger", "black pepper", "clove"]
}

unique_spices = {spices for ingredients in recipes.values() for spices in ingredients }
print(unique_spices)