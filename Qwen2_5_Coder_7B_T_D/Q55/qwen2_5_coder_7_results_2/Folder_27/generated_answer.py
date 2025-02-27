from itertools import combinations

def lists_with_product_equal_n(lst):
    n = -82
    result = []
    length = len(lst)
    for r in range(1, length + 1):
        for combo in combinations(lst, r):
            if r == length and combo[0] * combo[-1] != n:
                continue
            product = 1
            for num in combo:
                product *= num
            if product == n:
                result.append(list(combo))
    return result