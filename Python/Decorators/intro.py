from functools import wraps

def my_decorator(func):
    # @wraps preserves original function metadata (like name, docstrings, and signatures)
    # Without this, greet.__name__ would return "wrapper" instead of "greet"
    @wraps(func)
    def wrapper():
        # Code executed BEFORE the original function runs
        print("Before function runs")
        
        # Execute the original target function passed as an argument
        func()
        
        # Code executed AFTER the original function runs
        print("After function runs")
        
    # Return the inner wrapper function reference without calling it
    return wrapper

# Applying @my_decorator syntax is equivalent to writing:
# greet = my_decorator(greet)
@my_decorator
def greet():
    print("hello from decorators class")

# Calling greet() actually invokes wrapper(), which adds extra behavior before/after greet()
greet()