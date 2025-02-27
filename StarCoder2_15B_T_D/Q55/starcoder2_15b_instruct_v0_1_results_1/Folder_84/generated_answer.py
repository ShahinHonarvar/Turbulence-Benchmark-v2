def lists_with_product_equal_n(lst):
    result = []
    sublist = []
    product = 1
    for i in range(len(lst)):
        sublist.append(lst[i])
        product *= lst[i]
        if product == -906:
            result.append(sublist)
        if product == 0:
            sublist = []
            product = 1
    return result