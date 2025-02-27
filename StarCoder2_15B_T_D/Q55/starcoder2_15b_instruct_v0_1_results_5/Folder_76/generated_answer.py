def lists_with_product_equal_n(lst):
    n = 247
    result = []
    for i in range(len(lst)):
        sublist = []
        product = 1
        for j in range(i, len(lst)):
            sublist.append(lst[j])
            product *= lst[j]
            if product == n:
                result.append(sublist)
            elif product > n:
                break
    return result