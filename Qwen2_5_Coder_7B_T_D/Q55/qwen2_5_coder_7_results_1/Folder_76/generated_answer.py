def lists_with_product_equal_n(lst):
    n = 247
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, i + len(lst)):
            product *= lst[j % len(lst)]
            if product == n:
                result.append(lst[i:j % len(lst) + 1])
            elif product > n:
                break
    return result