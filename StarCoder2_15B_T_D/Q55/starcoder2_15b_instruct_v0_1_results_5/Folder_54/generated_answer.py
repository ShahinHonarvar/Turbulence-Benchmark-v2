def lists_with_product_equal_n(lst):
    result = []
    for size in range(1, len(lst) + 1):
        for start in range(len(lst)):
            sublist = lst[start:start + size]
            if len(sublist) < size:
                sublist += lst[:size - len(sublist)]
            product = 1
            for num in sublist:
                product *= num
            if product == -17:
                result.append(sublist)
    return result