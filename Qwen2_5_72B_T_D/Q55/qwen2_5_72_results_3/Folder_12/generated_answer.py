def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            end = (start + length) % n
            sublist = circular_list[start:] + circular_list[:end]
            if len(sublist) == length and product(sublist) == -18:
                result.append(sublist)
    return result

def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod