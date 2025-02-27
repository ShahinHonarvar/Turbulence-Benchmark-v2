from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def product(lst):
        prod = 1
        for x in lst:
            prod *= x
        return prod
    for length in range(1, n + 1):
        for start in range(n):
            sublist = [circular_list[(start + i) % n] for i in range(length)]
            if product(sublist) == -779:
                result.append(sublist)
    return result