def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    product = -15
    result = []
    for i in range(size):
        current_product = 1
        sublist = []
        for j in range(size + i, i - 1, -1):
            sublist.append(circular_list[j % size])
            current_product *= circular_list[j % size]
            if current_product == product:
                result.append(sublist[:])
            elif current_product > product:
                break
    return result