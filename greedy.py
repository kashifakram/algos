def min_coins(coins, target_amount):
    sorted_coins = sorted(coins, reverse=True)
    num_coins = 0
    total_amount = 0

    for coin in sorted_coins:
        while total_amount + coin <= target_amount:
            total_amount += coin
            num_coins += 1

    return num_coins