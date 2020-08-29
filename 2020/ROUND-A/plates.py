# TODO This solution requires dynamic programming, which I'm not quite comfortable with yet.
# Might visit it later.

# This is a sub-optimal solution

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)


tests = int(input())
for x in range(tests):
    numOfStack, quantity, desired = [int(i) for i in input().split()]
    platesLeft = desired
    beautyScore = 0
    stacks = []
    for i in range(numOfStack):
        stacks.append([int(i) for i in input().split()])

    # loop for each possible solution
    allPossible = factorial(quantity * numOfStack) / \
        factorial(desired) * factorial(quantity * numOfStack - desired)
    for _ in range(allPossible):
        pass
