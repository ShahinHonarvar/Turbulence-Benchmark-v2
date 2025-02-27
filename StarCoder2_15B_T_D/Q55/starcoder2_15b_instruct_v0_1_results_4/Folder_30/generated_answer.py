def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + i + 1):
            sublist = lst[i:j]
            if len(sublist) > len(lst):
                break
            if len(sublist) > 1 and len(sublist) <= len(lst) and (99 % len(sublist) == 0):
                if 99 / len(sublist) == 1 or all((x == 1 for x in sublist)):
                    result.append(sublist)
    return result