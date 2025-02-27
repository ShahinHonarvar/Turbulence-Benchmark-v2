def lists_with_product_equal_n(lst):
    n = 90
    result = []
    size = len(lst)
    lst = lst + lst
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j])
    return result