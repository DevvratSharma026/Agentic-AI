# Dictionary: A collection of key-value pairs, where each key is unique and maps to a specific value. Dictionaries are unordered, changeable, and indexed. They are written with curly braces {} and consist of key-value pairs separated by a colon (:).

my_dict = {
    "name": "Dev", 
    "age": 23,
    "role": "OIC Specialist",
    "future plan": {
        "role": "Forward Deployed Engineer",
        "company": "OpenAI"
    }
}

print(my_dict.keys())
print(my_dict.values())

# items(): returns a view object that displays a list of a dictionary's key-value tuple pairs. This view object can be used to iterate over the dictionary's items, allowing you to access both keys and values simultaneously.
print(my_dict.items())


# you can also create a dictionary using the dict() constructor, which allows you to create a dictionary from a sequence of key-value pairs or from keyword arguments. This can be useful when you want to create a dictionary dynamically or when you have data in a different format that you want to convert into a dictionary.
chai_order = dict(type="chai", size="medium", sugar=True, milk=True)

print(f"chai order: {chai_order}")

my_dict["working location"] = "Noida" # adding a new key-value pair to the dictionary

extra_values = {"hobby": "coding", "language": "python"}
my_dict.update(extra_values) # updating the dictionary with another dict
