def lists_with_product_equal_n(lst):
    n = -16
    result = []
    lst = lst + lst
    for i in range(len(lst)):
        product = 1
        for j in range(i, min(i + len(lst) // 2, len(lst))):
            product *= lst[j % len(lst)]
            if product == n:
                result.append(lst[i:j % len(lst) + 1])
                break
    return result