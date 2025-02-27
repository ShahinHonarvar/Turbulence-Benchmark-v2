def lists_with_product_equal_n(circular_list):
    n = 91
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, len(circular_list) + i):
            product *= circular_list[j % len(circular_list)]
            sublist.append(circular_list[j % len(circular_list)])
            if product == n:
                result.append(sublist.copy())
                break
            elif product > n:
                break
    return result