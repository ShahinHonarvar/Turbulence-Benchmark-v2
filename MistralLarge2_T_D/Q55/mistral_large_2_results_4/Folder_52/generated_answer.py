def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            idx = (i + j) % n
            product *= circular_list[idx]
            sublist.append(circular_list[idx])
            if product == 37:
                result.append(sublist[:])
            elif product > 37:
                break
    return result