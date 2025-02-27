def lists_with_product_equal_n(circular_list):
    n = -57
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, i + len(circular_list)):
            product *= circular_list[j % len(circular_list)]
            sublist.append(circular_list[j % len(circular_list)])
            if product == n:
                sublists.append(sublist)
                break
            if product == 0:
                break
    return sublists