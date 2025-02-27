def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            sublist = circular_list[i:j % n]
            if 0 in sublist:
                result.append(sublist)
    return result