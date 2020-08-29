# TODO This solution requires dynamic programming, which I'm not quite comfortable with yet.
# Might visit it later.

# This is a sub-optimal solution

# recursive factorial

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)


# factorial using dynamic programming
memo = {}


def dynamicFactorial(num):
    global memo

    if num in memo:
        return memo[num]

    if num == 1:
        return 1

    result = num * factorial(num - 1)
    memo[num] = result
    return result


# tests = int(input())
# for x in range(tests):
#     numOfStack, quantity, desired = [int(i) for i in input().split()]
#     platesLeft = desired
#     beautyScore = 0
#     stacks = []
#     for i in range(numOfStack):
#         stacks.append([int(i) for i in input().split()])

#     # loop for each possible solution
#     allPossible = factorial(quantity * numOfStack) / \
#         factorial(desired) * factorial(quantity * numOfStack - desired)
#     for _ in range(allPossible):
#         pass
