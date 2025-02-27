def lists_with_product_equal_n(circular_list, n=-779):
    product = 1
    result = []
    sublist = []
    size = len(circular_list)
    for i in range(size * 2):
        idx = i % size
        product *= circular_list[idx]
        sublist.append(circular_list[idx])
        if product == n:
            result.append(sublist[:])
        elif product > n:
            while product > n and sublist:
                product /= sublist.pop(0)
        if len(sublist) > 1 and sublist[0] * product == n:
            result.append(sublist[:])
    return result