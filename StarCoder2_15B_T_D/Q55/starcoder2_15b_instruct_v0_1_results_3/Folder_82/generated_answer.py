def lists_with_product_equal_n(circular_list):
    circular_list.append(circular_list[0])
    sublists = []
    for i in range(len(circular_list) - 1):
        for j in range(i + 1, len(circular_list)):
            product = 1
            for k in range(i, j):
                product *= circular_list[k]
            if product == 8:
                sublists.append(circular_list[i:j])
    return sublists