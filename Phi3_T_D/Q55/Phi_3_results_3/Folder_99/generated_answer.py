def lists_with_product_equal_n(circular_list):
    n = 415
    result = []
    for i in range(len(circular_list)):
        product = 1
        j = i
        sublist = []
        while product != n:
            if j >= len(circular_list):
                j = 0
            sublist.append(circular_list[j])
            product *= circular_list[j]
            if product > n:
                break
            j += 1
        if product == n:
            result.append(sublist)
    return result