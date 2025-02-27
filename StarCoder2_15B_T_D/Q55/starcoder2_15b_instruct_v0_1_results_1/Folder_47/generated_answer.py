def lists_with_product_equal_n(lst):
    result = set()
    for i in range(len(lst)):
        for j in range(1, len(lst) + 1):
            sublist = lst[i:i + j]
            if len(sublist) > 0 and len(sublist) <= len(lst) and (1 == abs(94 // reduce(lambda x, y: x * y, sublist))):
                result.add(tuple(sublist))
    return [list(x) for x in result]