def lists_with_product_equal_n(lst):
    n = 45
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
            elif product > n:
                break
    return result