def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == -23:
                result.append(lst[i:(i + j + 1) % n] if (i + j + 1) % n != i else lst[i:] + lst[:i])
    return result