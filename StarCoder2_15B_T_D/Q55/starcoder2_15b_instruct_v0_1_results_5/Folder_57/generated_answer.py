def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    product = 1
    for i in range(n):
        product *= circular_list[i]
    if product == -75:
        return [circular_list]
    sublists = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= circular_list[j % n]
            if product == -75:
                sublists.append(circular_list[i:j % n + 1])
    return sublists