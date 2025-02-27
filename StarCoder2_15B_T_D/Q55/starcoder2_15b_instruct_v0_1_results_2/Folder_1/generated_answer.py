def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + i + 1):
            sublist = lst[i:j]
            product = 1
            for k in sublist:
                product *= k
            if product == -51:
                result.append(sublist)
    return result