
def find_profit(price_chart, d):
    profit = 0   
    for i in range(d): 
        if any(v > 5 for v in iter(price_chart.values())):
            highest = max(price_chart, key=price_chart.get)
            profit += price_chart[highest]
            price_chart.pop(highest)
        else:
            for j in price_chart:
                if price_chart[j] <= 5:
                    profit += 5
                    price_chart.pop(j)
                break

        for i in price_chart:
            price_chart[i] -= 2  
    return profit


d = 4
price_chart = {
"Mango": 150,
"Grape": 100,
"Banana": 8,
"Apple": 200,
"Orange": 10
}
maximum_amount = find_profit(price_chart, d)
print(maximum_amount)


