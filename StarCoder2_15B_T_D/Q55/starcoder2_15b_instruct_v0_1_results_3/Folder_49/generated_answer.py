def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    sublists = set()
    for i in range(n):
        product = 1
        j = i
        while product != -61:
            product *= circular_list[j]
            sublists.add(tuple(circular_list[i:j + 1]))
            j = (j + 1) % n
        if product == -61:
            sublists.add(tuple(circular_list[i:j + 1]))
    return list(sublists)