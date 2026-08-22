tea_prices_inr = {
    "masala chai": 40,
    "green tea": 60,
    "ginger tea": 30,
}

#converting inr to dollar using comprehension

tea_prices_usd = { tea: price/90 for tea, price in tea_prices_inr.items() }
print(tea_prices_usd)