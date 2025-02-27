def lists_with_product_equal_n(circular_list):
    n = -41
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        sublist = []
        for i in range(length):
            current_index = (start + i) % length
            product *= circular_list[current_index]
            if product == n:
                sublist.append(circular_list[current_index])
                result.append(sublist)
                sublist = []
                product = 1
            elif product > n:
                sublist = []
                product = 1
    return result