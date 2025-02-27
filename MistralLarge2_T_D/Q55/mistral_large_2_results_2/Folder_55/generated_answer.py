def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    lst = lst * 2
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j]
            if product == -6:
                result.append(lst[i:j + 1])
    return result