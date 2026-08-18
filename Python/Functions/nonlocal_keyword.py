#nonlocal keyword in python allows a nested function to modify variables from its nearest ecnclosing(non-global) scope. You can declare multiple variables as nonlocal in a single statement, enabling simultaneous updates to sevral outer-scope variables.

def outer():
    a=2
    def inner():
        nonlocal a
        a += 5
        print(f'Inner {a}')
    inner()
    print(f'outside {a}')
outer()