def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    product = 46
    result = []
    for i in range(n):
        current_product = 1
        sublist = []
        for j in range(n):
            current_product *= circular_list[(i + j) % n]
            sublist.append(circular_list[(i + j) % n])
            if current_product == product:
                result.append(sublist[:])
            if current_product > product:
                break
    return result