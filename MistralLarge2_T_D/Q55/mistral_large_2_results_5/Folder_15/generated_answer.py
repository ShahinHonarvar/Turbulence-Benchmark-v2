def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            product *= lst[(i + j) % n]
            sublist.append(lst[(i + j) % n])
            if product == -7:
                result.append(sublist[:])
    return result