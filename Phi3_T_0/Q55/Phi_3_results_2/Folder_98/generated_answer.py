def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1] + circular_list[:i]
            if len(sublist) <= n and all((x == -1 for x in sublist)):
                result.append(sublist)
    return result