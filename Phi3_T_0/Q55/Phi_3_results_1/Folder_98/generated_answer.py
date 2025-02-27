def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            sublist = circular_list[i:j % n]
            if len(sublist) > 0 and -1 == functools.reduce(lambda x, y: x * y, sublist):
                result.append(sublist)
    return result