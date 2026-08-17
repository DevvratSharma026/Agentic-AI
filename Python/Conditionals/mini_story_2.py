print("HELLO WELCOME TO THE SHARMAJI SHOP!")

snack = input("Enter you preffered snack: ").lower()

if snack == 'samosa' or snack == 'cookie':
    print(f'{snack} is available take from counter')
else:
    print(f'Sorry {snack} not available')