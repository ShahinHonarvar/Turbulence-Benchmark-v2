def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            product *= circular_list[(i + j) % n]
            sublist.append(circular_list[(i + j) % n])
            if product == -5:
                result.append(sublist[:])
            if product != -5 and abs(product) > 5:
                break
    return result