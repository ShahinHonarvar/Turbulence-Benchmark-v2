def lists_with_product_equal_n(circular_list):
    product_target = 65
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == -product_target:
                result.append(sublist.copy())
                break
            elif product > -product_target:
                break
    return result