def lists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            product = 1
            for k in sublist:
                product *= k
            if product == n:
                result.append(sublist)
    return result