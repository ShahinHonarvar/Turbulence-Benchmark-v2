def lists_with_product_equal_n(circular_list):
    result = []
    n = 632
    size = len(circular_list)
    for i in range(size):
        product = 1
        sublist = []
        for j in range(i, i + size):
            index = j % size
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == n:
                result.append(sublist)
                break
            elif product > n:
                break
    return result