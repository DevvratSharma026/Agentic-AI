#Generator comprehension is like a stream of data unlike everyother comprehension it does not throw value at once it gives a flow, this is a memory efficient comprehension/code

daily_sales = [2, 45, 89, 22, 12, 90, 23]

total_cups = sum( sale for sale in daily_sales if sale > 30 )
print(total_cups)