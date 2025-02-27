def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    result = []
    i = 0
    while i < size:
        product = 1
        temp_list = []
        for j in range(i, i + size):
            temp_list.append(circular_list[j % size])
            product *= circular_list[j % size]
            if product == 733:
                result.append(temp_list)
                break
            elif product > 733:
                break
        i += 1
    return result