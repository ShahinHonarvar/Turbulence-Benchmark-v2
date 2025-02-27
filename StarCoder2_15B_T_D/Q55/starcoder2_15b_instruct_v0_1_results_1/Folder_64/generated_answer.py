def lists_with_product_equal_n(circular_list, n):
    result = []
    size = len(circular_list)
    for i in range(size):
        sublist = []
        product = 1
        for j in range(i, i + size):
            index = j % size
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == n:
                result.append(sublist)
            elif product > n:
                break
    return result