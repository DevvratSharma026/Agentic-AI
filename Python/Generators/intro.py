#Generators: we use 'yield' keyword
def server_chai():
    yield "cup1: Masala chai"
    yield "cup2: ginger tea"
    yield "cup3: lemon tea"
    
stall = server_chai()
# print(stall)
   #print this and see it shows: <generator object server_chai at 0x000001BDD75D4930>, it denotes it just holds the reference until it is looped over
   
#like this you can see it resumes from where we left in the yield 
# print(next(stall))
# print(next(stall))



for cup in stall:
    print(cup)
    
# Normal Function:   [ Cup 1 , Cup 2 , Cup 3 ]  --> Stores entire list in RAM at once
# Generator:         State Paused ---> Yield Cup 1 ---> State Paused ---> Yield Cup 2 ... (RAM holds 1 item at a time)