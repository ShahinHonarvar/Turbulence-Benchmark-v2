def lists_with_product_equal_n(lst):
    n = 83
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, length + i):
            product *= lst[j % length]
            if product == n:
                result.append(lst[i:j % length])
            elif product > n:
                break
    return result