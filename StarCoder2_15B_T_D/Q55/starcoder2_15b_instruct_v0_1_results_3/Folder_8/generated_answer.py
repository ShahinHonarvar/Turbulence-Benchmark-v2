from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = -41
    sublists = []
    for length in range(1, len(circular_list) + 1):
        for combination in combinations(circular_list, length):
            if n % product(combination) == 0:
                sublists.append(combination)
    return sublists

def product(iterable):
    return 1 if not iterable else iterable[0] * product(iterable[1:])