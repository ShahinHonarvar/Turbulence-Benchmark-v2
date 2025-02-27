def lists_with_product_equal_n(lst):
    n = -51
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, i + len(lst)):
            index = j % len(lst)
            product *= lst[index]
            sublist.append(lst[index])
            if product == n:
                result.append(sublist)
            if product == 0 or product == 1:
                break
    return result