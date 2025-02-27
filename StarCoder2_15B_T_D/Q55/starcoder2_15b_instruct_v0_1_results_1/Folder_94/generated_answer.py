def lists_with_product_equal_n(circular_list):
    n = -30
    sublists = []
    for start_index in range(len(circular_list)):
        product = 1
        sublist = []
        for i in range(start_index, start_index + len(circular_list)):
            index = i % len(circular_list)
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == n:
                sublists.append(sublist)
                break
            if product == 0:
                break
    return sublists