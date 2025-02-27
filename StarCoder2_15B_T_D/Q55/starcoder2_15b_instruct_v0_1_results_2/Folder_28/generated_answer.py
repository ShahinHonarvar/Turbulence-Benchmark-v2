def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, i + len(circular_list)):
            index = j % len(circular_list)
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == 85:
                sublists.append(sublist)
                break
            if product > 85:
                break
    return sublists