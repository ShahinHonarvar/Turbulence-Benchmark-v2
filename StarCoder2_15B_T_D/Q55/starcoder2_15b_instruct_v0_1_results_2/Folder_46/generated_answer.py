def lists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        sublist = [lst[i]]
        prod = lst[i]
        for j in range(i + 1, len(lst) + i):
            sublist.append(lst[j % len(lst)])
            prod *= lst[j % len(lst)]
            if prod == n:
                result.append(sublist)
                break
            elif prod > n:
                break
    return result