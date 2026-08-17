serve_size = input("Enter your serve size: ").lower()
price = 0

if serve_size == 'small':
    price = 5
elif serve_size == 'medium':
    price = 10
elif serve_size == 'large':
    price = 15
else:
    print("size not availabe")
    
if price:
    print(f"{price} rupees for your {serve_size} tea")