flavours = ['ginger', 'lemon', 'out of stock', 'tulsi', 'discontinued']

for flavour in flavours:
    if flavour == 'out of stock':
        continue
    if flavour == 'discontinued':
        print('discontinued item found')
        break
else:
    print('did not break the loop') # this else will only run if the loop did not break, if it got break it will not run     
