
def max_profit(futurePrices):
    # futurePrices: [10, 15, 7, 10, 13, 5, 7]
    # Maximize stock profit using only one buy-sell transaction
    
    maxProfit = 0
    minPrice = futurePrices[0]
    for time in range(len(futurePrices)):
        currentPrice = futurePrices[time]
        minPrice = min(minPrice, currentPrice)
        maxProfit = max(maxProfit, currentPrice - minPrice)
        
    return maxProfit
        
    #O(n) for time
    #O(1) space
    
