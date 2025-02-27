def lists_with_product_equal_n(circular_list):
    n = -16
    result = []
    size = len(circular_list)
    for start in range(size):
        product = 1
        sublist = []
        for i in range(start, start + size):
            index = i % size
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == n:
                result.append(sublist)
                break
            elif product == 0:
                break
    return result