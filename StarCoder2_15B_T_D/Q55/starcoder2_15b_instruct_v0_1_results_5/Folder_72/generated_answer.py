from itertools import combinations

def lists_with_product_equal_n(lst, n):
    sublists = []
    for i in range(1, len(lst) + 1):
        for combination in combinations(lst, i):
            if len(combination) <= len(lst) and len(combination) > 0:
                if n == 1:
                    sublists.append(list(combination))
                elif n % len(combination) == 0:
                    if n // len(combination) == 1:
                        sublists.append(list(combination))
                    else:
                        product = 1
                        for num in combination:
                            product *= num
                        if product == n // len(combination):
                            sublists.append(list(combination))
    return sublists