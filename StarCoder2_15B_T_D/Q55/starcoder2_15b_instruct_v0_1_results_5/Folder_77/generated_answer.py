def lists_with_product_equal_n(circular_list, n):

    def circular_index(i):
        return i % len(circular_list)
    sublists = []
    for i in range(len(circular_list)):
        current_product = 1
        current_sublist = []
        for j in range(i, i + len(circular_list)):
            current_product *= circular_list[circular_index(j)]
            current_sublist.append(circular_list[circular_index(j)])
            if current_product == n:
                sublists.append(current_sublist)
                break
            elif current_product > n:
                break
    return sublists