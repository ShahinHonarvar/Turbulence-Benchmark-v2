def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            if len(sublist) <= n and 1 in sublist:
                product = 1
                for k in sublist:
                    product *= k
                if product == -69:
                    result.append(sublist)
    return result