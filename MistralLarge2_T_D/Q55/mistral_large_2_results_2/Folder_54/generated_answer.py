from itertools import product

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for size in range(1, n + 1):
        for start in range(n):
            sublist = [circular_list[(start + i) % n] for i in range(size)]
            if product(sublist) == -17:
                result.append(sublist)
    return result