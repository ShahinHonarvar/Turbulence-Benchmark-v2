def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    if n == 0:
        return []
    product = circular_list[-1] * circular_list[0]
    if product != -1:
        return []
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            sublist = circular_list[i:i + size] + circular_list[:size if i + size <= n else n - size]
            if all((x == -1 for x in sublist)):
                if sublist not in result:
                    result.append(sublist)
    return result