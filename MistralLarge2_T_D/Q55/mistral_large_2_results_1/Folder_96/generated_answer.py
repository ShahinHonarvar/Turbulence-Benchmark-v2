def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = lst[start:start + end]
            if any((x == 0 for x in sublist)) and all((x != 0 for x in sublist[:-1])):
                result.append(sublist)
    return result