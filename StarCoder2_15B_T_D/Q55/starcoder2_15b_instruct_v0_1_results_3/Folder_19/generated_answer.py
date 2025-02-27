def lists_with_product_equal_n(circular_list):

    def circular_index(i):
        return i % len(circular_list)
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, i + len(circular_list)):
            sublist.append(circular_list[circular_index(j)])
            product *= circular_list[circular_index(j)]
            if product == -54:
                sublists.append(sublist[:])
            elif product > -54:
                break
    return sublists