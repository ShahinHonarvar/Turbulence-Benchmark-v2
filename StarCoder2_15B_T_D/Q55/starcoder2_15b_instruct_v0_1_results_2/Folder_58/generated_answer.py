def lists_with_product_equal_n(circular_list):
    sublists = []
    for start_index in range(len(circular_list)):
        product = 1
        sublist = []
        for i in range(start_index, start_index + len(circular_list)):
            index = i % len(circular_list)
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == 733:
                sublists.append(sublist)
                break
            elif product > 733:
                break
    return sublists