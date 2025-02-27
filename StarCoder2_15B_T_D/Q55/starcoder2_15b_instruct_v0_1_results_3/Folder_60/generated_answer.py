def list_with_product_equal_n(lst, n):
    product = 1
    start = 0
    result = []
    for i in range(len(lst)):
        product *= lst[i]
        while product > n:
            product /= lst[start]
            start += 1
        if product == n:
            result.append(lst[start:i + 1])
    return result