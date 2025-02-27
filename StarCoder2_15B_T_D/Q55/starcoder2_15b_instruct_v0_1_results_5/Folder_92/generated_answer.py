def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n + i):
            sublist = lst[i:j]
            if len(sublist) > n:
                break
            product = 1
            for k in sublist:
                product *= k
            if product == 5:
                result.append(sublist)
    return result