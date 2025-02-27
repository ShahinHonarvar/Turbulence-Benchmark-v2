def lists_with_product_equal_n(circular_list):
    product = 1
    target_product = -51
    sublists = []
    size = len(circular_list)
    for i in range(size):
        product = 1
        for j in range(size):
            product *= circular_list[(i + j) % size]
            if product == target_product:
                sublists.append(circular_list[i:j + 1])
    return sublists