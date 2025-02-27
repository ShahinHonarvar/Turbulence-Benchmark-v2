def lists_with_product_equal_n(circular_list):
    n = 27
    length = len(circular_list)
    result = []
    for i in range(length):
        product = 1
        sublist = []
        for j in range(length):
            product *= circular_list[(i + j) % length]
            sublist.append(circular_list[(i + j) % length])
            if product == n:
                result.append(sublist[:])
            elif product > n:
                break
    return result