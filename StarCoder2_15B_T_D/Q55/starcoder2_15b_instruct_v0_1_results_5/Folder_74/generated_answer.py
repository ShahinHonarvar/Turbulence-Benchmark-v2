def lists_with_product_equal_n(lst):
    n = 51
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if len(sublist) <= len(lst) and n % len(sublist) == 0 and (n // len(sublist) == sum(sublist)):
                result.append(sublist)
    return result