def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            index = j % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == -18:
                sublists.append(sublist)
                break
    return sublists