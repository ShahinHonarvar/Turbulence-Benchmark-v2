from itertools import product

def lists_with_product_equal_n(circular_list):
    n = -81
    result = []
    list_len = len(circular_list)
    for i in range(list_len):
        for size in range(1, list_len + 1):
            for j in range(list_len):
                sublist = circular_list[j:j + size]
                if j + size > list_len:
                    sublist += circular_list[:j + size - list_len]
                if all((x != 0 and n % x == 0 for x in sublist)) and prod(sublist) == n:
                    result.append(sublist)
    return result

def prod(iterable):
    product = 1
    for x in iterable:
        product *= x
    return product