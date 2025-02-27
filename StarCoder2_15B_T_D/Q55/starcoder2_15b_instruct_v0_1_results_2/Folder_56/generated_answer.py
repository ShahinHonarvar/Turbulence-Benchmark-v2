def lists_with_product_equal_n(lst):
    n = -65
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i == j - 1:
                continue
            sublist = lst[i:j]
            if len(sublist) == 1:
                continue
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result