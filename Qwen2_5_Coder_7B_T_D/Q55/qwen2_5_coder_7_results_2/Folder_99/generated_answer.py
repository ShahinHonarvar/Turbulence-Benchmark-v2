def lists_with_product_equal_n(l):
    n = 415
    result = []
    nlen = len(l)
    for i in range(nlen):
        product = 1
        for j in range(i, nlen):
            product *= l[j]
            if product == n:
                result.append(l[i:j + 1])
            elif product > n:
                break
    return result