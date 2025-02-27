def lists_with_product_equal_n(lst):
    n = 76
    result = []
    for i in range(len(lst)):
        prod = 1
        sublist = []
        for j in range(i, len(lst) + i):
            sublist.append(lst[j % len(lst)])
            prod *= sublist[-1]
            if prod == n:
                result.append(sublist.copy())
            elif prod > n:
                break
    return result