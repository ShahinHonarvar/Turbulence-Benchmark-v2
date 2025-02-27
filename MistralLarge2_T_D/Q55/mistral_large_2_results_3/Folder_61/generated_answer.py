def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            product *= circular_list[(i + j) % n]
            sublist.append(circular_list[(i + j) % n])
            if product == -10:
                result.append(sublist[:])
            elif product != -10 and abs(product) > 10:
                break
    return result