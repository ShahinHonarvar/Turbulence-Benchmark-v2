def lists_with_product_equal_n(circular_list, n=-83):
    size = len(circular_list)
    result = []
    for i in range(size):
        product = 1
        sublist = []
        for j in range(size):
            product *= circular_list[(i + j) % size]
            sublist.append(circular_list[(i + j) % size])
            if product == n:
                result.append(sublist[:])
            if product != n and product % n != 0 and (product != 1):
                break
    return result