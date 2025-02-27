def lists_with_product_equal_n(lst):
    n = -54
    result = []
    for i in range(len(lst)):
        prod = 1
        sublist = []
        for j in range(i, i + len(lst)):
            num = lst[j % len(lst)]
            prod *= num
            sublist.append(num)
            if prod == n:
                result.append(sublist)
                break
            elif prod > n:
                break
    return result