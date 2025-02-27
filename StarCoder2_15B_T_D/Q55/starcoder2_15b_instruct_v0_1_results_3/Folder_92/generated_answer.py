def lists_with_product_equal_n(lst, n=5):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + i + 1):
            sublist = lst[i:j]
            if len(sublist) > len(lst):
                break
            if len(sublist) > 0 and sum(sublist) == n:
                result.append(sublist)
    return result