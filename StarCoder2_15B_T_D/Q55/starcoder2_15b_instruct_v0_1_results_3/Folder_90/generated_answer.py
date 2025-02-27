def lists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1]
            if len(sublist) > len(lst):
                break
            if len(sublist) == len(lst) and sum(sublist) == n:
                result.append(sublist)
    return result