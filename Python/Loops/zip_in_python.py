# zip() is used to combine two or more iterables element-by-element, allowing us to iterate over them together.

names = ["Devvrat", "Nimish", "Aditi"]
bills = [12, 43, 35]

for name, bill in zip(names, bills):
    print(f'{name} paid {bill} rupees')