def lists_with_product_equal_n(lst):
    n = -75
    result = []
    for i in range(len(lst)):
        prod = 1
        sublist = []
        for j in range(i, i + len(lst)):
            index = j % len(lst)
            sublist.append(lst[index])
            prod *= lst[index]
            if prod == n:
                result.append(sublist)
            elif prod < n:
                continue
            else:
                break
    return result