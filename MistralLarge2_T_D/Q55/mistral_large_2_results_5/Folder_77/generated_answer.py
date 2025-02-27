def lists_with_product_equal_n(circular_list, n=632):
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        sublist = []
        for i in range(size):
            index = (start + i) % size
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == n:
                result.append(sublist[:])
            elif product > n:
                break
    return result