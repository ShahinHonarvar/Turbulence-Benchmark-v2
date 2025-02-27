def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        window = []
        product = 1
        for j in range(i, i + n):
            window.append(lst[j % n])
            product *= lst[j % n]
            if product == 0:
                result.append(window.copy())
    return result