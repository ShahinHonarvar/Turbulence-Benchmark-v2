from itertools import cycle, combinations

def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for sublist in combinations(cycle(nums), i + 1):
            if sum(sublist) * (i + 1) == -46:
                result.append(list(sublist))
    return result