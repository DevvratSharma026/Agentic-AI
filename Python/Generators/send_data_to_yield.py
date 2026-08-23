def chai_customer():
    # Executed ONLY on the very first next() call (priming step)
    print("welcome")
    
    # --- PRIMING POINT ---
    # The generator pauses here during next(stall).
    # 'yield' yields None back to the caller and WAITS to receive a value via .send().
    # When stall.send("masala chai") is called, "masala chai" replaces this expression
    # and is assigned to the 'order' variable.
    order = yield
    
    # Enter the main serving loop
    while True:
        # Prints the order that was just sent into the generator
        print(f"preparing: {order}")
        
        # --- PAUSE POINT IN THE LOOP ---
        # 1. 'yield' pauses the loop and waits for the NEXT .send() call.
        # 2. When the caller executes stall.send("lemon chai"), that string 
        #    replaces 'yield' and overwrites the 'order' variable.
        # 3. Execution loops back up to the top of 'while True' to print the new order.
        order = yield


# --- GENERATOR INSTANTIATION & EXECUTION ---

# Creates the generator object. 
# Memory allocated, but NO CODE inside chai_customer() has executed yet!
stall = chai_customer()

# STEP 1: Priming the Generator (Crucial Step)
# Runs code up to the FIRST 'yield' (prints "welcome") and pauses.
# A generator MUST be at a yield expression before it can accept values via .send().
next(stall) 

# STEP 2: Sending the First Order
# Resumes execution at the first 'yield', assigns "masala chai" to 'order',
# enters the while loop, prints "preparing: masala chai", and pauses at the second 'yield'.
stall.send("masala chai")   

# STEP 3: Sending the Second Order
# Resumes execution at the second 'yield', assigns "lemon chai" to 'order',
# loops back, prints "preparing: lemon chai", and pauses at the second 'yield' again.
stall.send("lemon chai")