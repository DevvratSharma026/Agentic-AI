def infinite_chai():
    count = 1
    
    # An infinite loop—normally this would crash or freeze a program, 
    # but 'yield' pauses execution every time, preventing an infinite loop freeze!
    while True:
        # 1. Evaluates the f-string using the current value of 'count'
        # 2. YIELDS (returns) the string reference back to the caller
        # 3. PAUSES execution here and freezes the local variable state (e.g., current 'count')
        yield f"Refil #{count}"
        
        # When next() is called again, execution resumes RIGHT HERE:
        # Increment 'count' by 1, then the 'while True' loops back up to the next yield statement
        count += 1
        

# --- CREATING GENERATOR INSTANCES ---

# Calling the function returns a NEW generator object.
# The code inside 'infinite_chai()' HAS NOT STARTED RUNNING YET.
refill = infinite_chai()

# 'user2' is a completely independent generator instance with its own frame and local variables.
# It starts its own separate 'count' at 1 (though we don't call next(user2) in this script).
user2 = infinite_chai()


# --- FIRST LOOP: Requesting 3 refills ---

print("--- First Loop (3 calls) ---")
for _ in range(3):
    # next(refill) enters/resumes 'infinite_chai', runs until 'yield', pauses, and returns the string.
    # Output: Refil #1, Refil #2, Refil #3
    print(next(refill))

    
# --- SECOND LOOP: Requesting 5 MORE refills from the SAME generator ---

print("\n--- Second Loop (5 calls) ---")
for _ in range(5):
    # 'refill' DOES NOT reset! It remembers 'count' was at 3 from the previous loop.
    # It resumes right after the yield, increments count to 4, and continues yielding.
    # Output: Refil #4, Refil #5, Refil #6, Refil #7, Refil #8
    print(next(refill))