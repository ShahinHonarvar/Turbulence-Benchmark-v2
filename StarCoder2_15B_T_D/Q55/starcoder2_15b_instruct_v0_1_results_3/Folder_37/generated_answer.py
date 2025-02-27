def lists_with_product_equal_n(lst):
    n = -76
    result = []
    for i in range(len(lst)):
        sublist = []
        product = 1
        for j in range(i, i + len(lst)):
            index = j % len(lst)
            sublist.append(lst[index])
            product *= lst[index]
            if product == n:
                result.append(sublist)
            elif product < n:
                continue
            else:
                break
    return result