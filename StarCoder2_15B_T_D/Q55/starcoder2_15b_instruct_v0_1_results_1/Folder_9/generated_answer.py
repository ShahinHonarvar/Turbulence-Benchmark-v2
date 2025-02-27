def lists_with_product_equal_n(lst):
    n = -36
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if i == j:
                continue
            sublist = lst[i:j + 1]
            if len(sublist) > len(lst):
                continue
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result