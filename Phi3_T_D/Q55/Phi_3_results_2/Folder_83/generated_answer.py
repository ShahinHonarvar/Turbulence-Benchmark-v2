def lists_with_product_equal_n(circular_list):
    N = -57
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        j = i
        sublist = []
        while product != N:
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == N:
                sublists.append(sublist.copy())
            j = (j + 1) % len(circular_list)
            if len(sublist) > len(circular_list):
                break
    return sublists