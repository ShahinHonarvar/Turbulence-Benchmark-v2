from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for length in range(1, n + 1):
        for start in range(n):
            sublist = []
            for i in range(length):
                sublist.append(circular_list[(start + i) % n])
            if product(sublist) == -3:
                result.append(sublist)
    return result

def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod