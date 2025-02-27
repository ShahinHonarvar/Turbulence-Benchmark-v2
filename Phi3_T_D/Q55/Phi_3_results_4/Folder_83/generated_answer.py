def lists_with_product_equal_n(it):
    circular_list = list(it) + list(it)[0:1]
    n = -57
    sublists = []
    for i in range(len(circular_list)):
        prod = 1
        for j in range(i, len(circular_list)):
            prod *= circular_list[j % len(circular_list)]
            if prod == n:
                sublists.append(circular_list[i:j % len(circular_list) + 1])
    return sublists