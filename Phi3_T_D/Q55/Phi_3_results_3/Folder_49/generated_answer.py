def lists_with_product_equal_n(circular_list):
    is_circular_list = len(circular_list) > 0 and abs(circular_list[0] * circular_list[-1]) == 1
    if not is_circular_list:
        circular_list += circular_list
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list) + i):
            product *= circular_list[j % len(circular_list)]
            if product == 61:
                result.append(circular_list[i:j % len(circular_list) + 1])
            elif product > 61:
                break
    return result