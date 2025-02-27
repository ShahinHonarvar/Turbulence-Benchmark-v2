def lists_with_product_equal_n(circular_list, target_product=-83):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            product *= circular_list[(i + j) % n]
            sublist.append(circular_list[(i + j) % n])
            if product == target_product:
                result.append(sublist[:])
            if product != 1 and abs(product) > abs(target_product):
                break
    return result