def lists_with_product_equal_n(circular_list):
    n = -75
    sublists = []
    product = 1
    list_size = len(circular_list)
    for i in range(list_size * 2):
        product = 1
        for j in range(i, i + list_size):
            product *= circular_list[j % list_size]
            if product == n:
                sublists.append([circular_list[(j - i) % list_size] for j in range(i, i + j - i + 1)])
    return sublists[:list_size]