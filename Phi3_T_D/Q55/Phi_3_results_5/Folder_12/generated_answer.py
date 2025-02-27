def lists_with_product_equal_n(circle):
    n = -18
    results = []
    for i in range(len(circle)):
        product = 1
        sublist = []
        for j in range(i, len(circle) + i):
            product *= circle[j % len(circle)]
            sublist.append(circle[j % len(circle)])
            if product == n:
                results.append(sublist.copy())
                break
            if product > n:
                break
    return results