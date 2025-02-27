def lists_with_product_equal_n(circular_list):
    n = 43
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(len(circular_list)):
            idx = (i + j) % len(circular_list)
            product *= circular_list[idx]
            sublist.append(circular_list[idx])
            if product == n:
                result.append(sublist[:])
            elif product > n:
                break
    return result