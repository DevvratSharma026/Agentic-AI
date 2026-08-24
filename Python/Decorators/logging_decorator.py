#logger using decorator
from functools import wraps

def log_activity(func):
    #preserve values using wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type, milk = True):
    print(f"brewing {type} chai and milk {milk}")
    
brew_chai('Masala', True)