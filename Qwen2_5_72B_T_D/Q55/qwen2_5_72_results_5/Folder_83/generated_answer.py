from math import prod

def lists_with_product_equal_n(circular_list):
    n = -57
    sublists = []
    length = len(circular_list)
    for size in range(1, length + 1):
        for start in range(length):
            sublist = [circular_list[(start + i) % length] for i in range(size)]
            if prod(sublist) == n:
                sublists.append(sublist)
    return sublists