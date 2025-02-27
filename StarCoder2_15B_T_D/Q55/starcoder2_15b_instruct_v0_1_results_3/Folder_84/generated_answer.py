def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i + 1, n + i):
            sublist = circular_list[i:j]
            if len(sublist) <= n and product(sublist) == -906:
                result.append(sublist)
    return result

def product(iterable):
    return 1