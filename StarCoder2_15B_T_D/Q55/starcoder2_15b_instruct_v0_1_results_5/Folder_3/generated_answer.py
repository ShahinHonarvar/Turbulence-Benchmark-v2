from itertools import combinations

def lists_with_product_equal_n(lst):
    n = -22
    result = []
    for i in range(1, len(lst) + 1):
        for combination in combinations(lst, i):
            if i < len(lst) and combination[0] == lst[-1]:
                continue
            if i == len(lst) and combination[0] != lst[0]:
                continue
            if 1 in combination and len(combination) > 1:
                continue
            if len(combination) == 1 and combination[0] != 1:
                continue
            product = 1
            for num in combination:
                product *= num
            if product == n:
                result.append(list(combination))
    return result