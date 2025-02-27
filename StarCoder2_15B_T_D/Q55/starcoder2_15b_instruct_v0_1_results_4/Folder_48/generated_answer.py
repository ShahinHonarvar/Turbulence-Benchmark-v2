def lists_with_product_equal_n(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        sublist = []
        product = 1
        for j in range(i, i + len(circular_list)):
            sublist.append(circular_list[j % len(circular_list)])
            product *= circular_list[j % len(circular_list)]
            if product == n:
                result.append(sublist)
            elif product > n:
                break
    return result