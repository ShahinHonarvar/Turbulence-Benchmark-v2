from math import prod

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -690
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = circular_list[start:start + length] or circular_list[start:] + circular_list[:length - (n - start)]
            if prod(sublist) == target_product:
                result.append(sublist)
    return result