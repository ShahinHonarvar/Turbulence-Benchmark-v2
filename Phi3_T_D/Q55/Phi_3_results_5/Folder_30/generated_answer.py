def lists_with_product_equal_n(circular_list):
    n = 99
    sublists = []
    for i in range(len(circular_list)):
        prod = 1
        sublist = []
        for j in range(i, i + len(circular_list)):
            prod *= circular_list[j % len(circular_list)]
            sublist.append(circular_list[j % len(circular_list)])
            if prod == n:
                sublists.append(sublist[:])
                break
            elif prod > n:
                break
    return sublists