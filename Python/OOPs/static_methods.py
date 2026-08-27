class chaiUtils:
    # @staticmethod tells Python: "Do not pass 'self' (instance) or 'cls' (class) implicitly."
    # It turns this method into a regular function that just happens to live inside the class namespace.
    @staticmethod
    def clean_ingridients(text):
        # Notice there is no 'self' parameter here. 
        # It only operates on the explicit arguments passed to it ('text').
        return [item.strip() for item in text.split(",")]
    
raw = " water , milk ,  ginger  , honey "

# Creating an instance is perfectly legal, but completely unnecessary for static methods.
obj = chaiUtils()

# ✅ BEST PRACTICE: Call the static method directly using the Class name.
# No object creation required. This saves memory and makes the code's intent clear.
cleaned = chaiUtils.clean_ingridients(raw)
print(cleaned)  # Output: ['water', 'milk', 'ginger', 'honey']

# 💡 Note: You CAN call it via the instance too: print(obj.clean_ingridients(raw))
# Python will resolve it correctly, but using the Class name is preferred.