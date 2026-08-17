# The walrus operator (:=), is an assignment expression that lets you assign a value to a variable as part of an expression. This is useful when you want to both use and store a value without repeating the computation or function call.
value = 14

if (remainder := value%5):
    print(f"not divisible, remainder is: {remainder}")