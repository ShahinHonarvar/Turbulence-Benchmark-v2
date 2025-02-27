def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            product *= circular_list[(start + i) % n]
            sublist.append(circular_list[(start + i) % n])
            if product == -61:
                result.append(sublist[:])
            elif product != 0 and -61 % product != 0:
                break
    return result