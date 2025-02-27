def lists_with_product_equal_n(circular_list, n):
    sublists = []
    for i in range(len(circular_list)):
        sublist = []
        product = 1
        for j in range(i, i + len(circular_list)):
            index = j % len(circular_list)
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == n:
                sublists.append(sublist)
                break
            elif product > n:
                break
    return sublists