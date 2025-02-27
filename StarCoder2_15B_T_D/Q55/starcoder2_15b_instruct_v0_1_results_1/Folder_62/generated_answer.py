def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(1, len(lst) + 1):
            sublist = lst[i:i + j]
            if len(sublist) > len(lst):
                sublist = sublist[:len(lst)]
            if len(sublist) == 0:
                continue
            product = 1
            for num in sublist:
                product *= num
            if product == 100:
                result.append(sublist)
    return result