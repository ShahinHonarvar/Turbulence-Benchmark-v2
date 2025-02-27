def lists_with_product_equal_n(lst):
    result = []
    n = -91
    lst = lst * 2
    for i in range(len(lst)):
        product = 1
        for j in range(i, i + len(lst) // 2):
            product *= lst[j % len(lst)]
            if product == n:
                result.append(lst[i:j % len(lst) + 1])
    return result