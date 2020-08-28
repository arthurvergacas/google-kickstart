tests = int(input())

for x in range(tests):
    housesBought = 0
    numHouses, budget = [int(i) for i in input().split()]
    prices = [int(i) for i in input().split()]
    prices.sort()
    for i in range(numHouses):
        if prices[i] <= budget:
            housesBought += 1
            budget -= prices[i]
    print("Case #{}: {}".format(x + 1, housesBought))
