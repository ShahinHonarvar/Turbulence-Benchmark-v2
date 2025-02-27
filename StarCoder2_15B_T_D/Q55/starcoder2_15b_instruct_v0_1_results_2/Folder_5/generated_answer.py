def lists_with_product_equal_n(l):
    n = -33
    product = 1
    sublists = []
    for i in range(len(l)):
        product *= l[i]
        if product == n:
            sublists.append(l[i:])
            product = 1
        elif product > n:
            product = 1
    return sublists