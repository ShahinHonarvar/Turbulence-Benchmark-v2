from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = 74
    result = []
    size = len(circular_list)
    for i in range(size):
        for j in range(1, size + 1):
            sublist = list(islice(cycle(circular_list), i, i + j))
            if len(sublist) <= size and product(sublist) == n:
                result.append(sublist)
    return result

def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod