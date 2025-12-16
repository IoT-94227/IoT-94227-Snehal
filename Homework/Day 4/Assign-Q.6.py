prices = [105, 110, 108, 112, 115, 116, 114]

rolling_avg = [
    sum(prices[i:i+3]) / 3
    for i in range(len(prices) - 2)
]

print(rolling_avg)
