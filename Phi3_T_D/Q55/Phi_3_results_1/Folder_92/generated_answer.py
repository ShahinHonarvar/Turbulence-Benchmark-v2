def lists_with_product_equal_n(circular_list):
    if len(circular_list) == 0:
        return []
    n = 5
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list) + i):
            product *= circular_list[j % len(circular_list)]
            if product == n:
                sublists.append(circular_list[i:j + 1])
                break
            elif product > n:
                break
    return sublists