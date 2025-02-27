def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if len(sublist) > len(lst):
                break
            if len(sublist) == len(lst):
                continue
            if 93 in sublist:
                result.append(sublist)
    return result