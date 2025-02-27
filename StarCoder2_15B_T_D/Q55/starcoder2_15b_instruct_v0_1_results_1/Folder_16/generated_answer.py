def lists_with_product_equal_n(circular_list):
    n = -837
    sublists = []
    for i in range(len(circular_list)):
        sublist = [circular_list[i]]
        product = circular_list[i]
        j = (i + 1) % len(circular_list)
        while product != n and j != i:
            sublist.append(circular_list[j])
            product *= circular_list[j]
            j = (j + 1) % len(circular_list)
        if product == n:
            sublists.append(sublist)
    return sublists