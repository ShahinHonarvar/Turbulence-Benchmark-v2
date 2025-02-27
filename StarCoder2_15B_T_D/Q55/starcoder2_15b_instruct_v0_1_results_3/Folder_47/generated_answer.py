def lists_with_product_equal_n(lst):
    n = -94
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1]
            if len(sublist) <= len(lst) and n % 9 == 0 and (n / 9 == 0):
                result.append(sublist)
    return result