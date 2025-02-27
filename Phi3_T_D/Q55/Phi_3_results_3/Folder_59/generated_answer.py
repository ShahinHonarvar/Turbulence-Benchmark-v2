def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    n = len(circular_list)
    product_target = -3
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(start, start + n):
            index = i % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == product_target:
                result.append(sublist.copy())
            elif product < product_target:
                break
    return result