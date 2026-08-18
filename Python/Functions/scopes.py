def serve_chai():
    chai_type = "masala" #local scope
    print(f"Inside function {chai_type}")

chai_type = "tulsi Tea" #gloal scope
serve_chai()
print(f"outside function {chai_type}")


def chai_counter():
    chai_order = 'lemon' #enclosing scope
    
    def print_order():
        chai_order = "ginger"
        print(f"inner: {chai_order} and chai type is {chai_type}")
    print_order()
    
    print(f'outer chai order: {chai_order}')
    
chai_counter()