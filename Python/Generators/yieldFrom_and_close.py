# ==========================================
# PART 1: 'yield from' (Generator Delegation)
# ==========================================

def local_chai():
    # Sub-generator 1
    yield "ginger tea"
    yield "masala chai"
    
def imported_chai():
    # Sub-generator 2
    yield "oolong tea"
    yield "matcha"

def all_chai():
    # 'yield from' delegates the iteration directly to another iterable/generator.
    # It acts as a transparent bi-directional pipe:
    # 1. Automatically consumes local_chai() until it raises StopIteration
    yield from local_chai()
    
    # 2. Once local_chai() is exhausted, seamlessly moves to imported_chai()
    yield from imported_chai()
    
teas = all_chai()

# The for loop iterates over the delegating generator 'all_chai()'.
# Behind the scenes, 'yield from' forwards each next() call to the active sub-generator
# and passes yielded values straight back to this loop.
for tea in teas:
    print(tea)
    # Output:
    # ginger tea
    # masala chai
    # oolong tea
    # matcha


# ==========================================
# PART 2: Generator .close() Method
# ==========================================

def chai_stall():
    try:
        while True:
            # Yields the status string out and waits for a .send() call
            order = yield "Waiting for your order"
    except GeneratorExit:
        # Calling .close() on the generator raises a GeneratorExit exception 
        # AT the point where the generator is currently paused (at the yield statement).
        # We can catch it to run cleanup logic!
        print("stall closed, chai khatam")
        
stall = chai_stall()

# STEP 1: Prime the generator
# Code runs until the first 'yield', returning "Waiting for your order" and pausing.
print(next(stall))  # Output: Waiting for your order

# STEP 2: Close the generator
# Injects GeneratorExit into the paused yield statement inside 'chai_stall()'.
# The exception is caught, prints "stall closed, chai khatam", and safely terminates the generator.
stall.close()