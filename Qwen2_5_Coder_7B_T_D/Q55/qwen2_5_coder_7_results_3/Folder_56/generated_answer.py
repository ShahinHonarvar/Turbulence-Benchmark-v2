def lists_with_product_equal_n(l):
    n = -65
    result = []
    for i in range(len(l)):
        product = 1
        for j in range(i, len(l) + i):
            product *= l[j % len(l)]
            if product == n:
                result.append(l[i:j % len(l)])
    return result