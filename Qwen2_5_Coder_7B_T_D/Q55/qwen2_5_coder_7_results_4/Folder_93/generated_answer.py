def lists_with_product_equal_n(lst):
    n = -91
    result = []
    for i in range(len(lst)):
        product = 1
        sublst = []
        for j in range(i, i + len(lst)):
            product *= lst[j % len(lst)]
            sublst.append(lst[j % len(lst)])
            if product == n:
                result.append(sublst)
                break
    return result