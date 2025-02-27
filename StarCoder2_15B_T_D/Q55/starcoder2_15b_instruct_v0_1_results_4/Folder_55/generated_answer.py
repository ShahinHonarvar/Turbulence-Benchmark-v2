def lists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + i + 1):
            sublist = lst[i:j]
            if len(sublist) > len(lst):
                break
            if len(sublist) == len(lst):
                sublist = sublist + sublist
            if len(sublist) > 0 and len(sublist) <= len(lst) and (n % len(sublist) == 0) and (n // len(sublist) == 1):
                result.append(sublist)
    return result