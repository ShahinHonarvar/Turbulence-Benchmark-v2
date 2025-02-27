def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        sublist = []
        product = 1
        for j in range(i, i + len(circular_list)):
            sublist.append(circular_list[j % len(circular_list)])
            product *= circular_list[j % len(circular_list)]
            if product == 48:
                sublists.append(sublist)
                break
            elif product > 48:
                break
    return sublists