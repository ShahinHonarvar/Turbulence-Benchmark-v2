def lists_with_product_equal_n(circular_list):
    n = 733
    result = []
    size = len(circular_list)
    for i in range(size):
        product = 1
        sublist = []
        for j in range(i, size + i):
            product *= circular_list[j % size]
            if product == n:
                sublist.append(circular_list[j % size])
                result.append(sublist.copy())
                product = 1
                sublist.clear()
                break
            elif product > n:
                break
            else:
                sublist.append(circular_list[j % size])
    return result