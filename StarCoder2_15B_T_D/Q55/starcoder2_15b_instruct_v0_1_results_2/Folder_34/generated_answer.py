def lists_with_product_equal_n(lst):
    n = -81
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
                break
            elif product == 0 or product > abs(n):
                break
    return result