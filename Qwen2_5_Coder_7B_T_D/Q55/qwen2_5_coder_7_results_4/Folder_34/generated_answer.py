def lists_with_product_equal_n(lst):
    n = -81
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= lst[j % size]
            if product == n:
                result.append(lst[i:j % size + 1])
                break
    return result