from itertools import combinations

def lists_with_product_equal_n(lst):
    n = -54
    result = []
    for i in range(len(lst)):
        for combo in combinations(lst[i:] + lst[:i], 2):
            if combo[0] * combo[1] == n:
                result.append(list(combo))
    return result