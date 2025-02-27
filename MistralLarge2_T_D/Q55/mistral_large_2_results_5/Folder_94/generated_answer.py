def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            product *= lst[(i + j) % n]
            sublist.append(lst[(i + j) % n])
            if product == -30:
                result.append(sublist[:])
            if product != -30 and abs(product) > 30:
                break
    return result