def lists_with_product_equal_n(lst):
    result = []
    n = -87
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, length):
            product *= lst[j % length]
            if product == n:
                result.append(lst[i:j + 1])
            elif product > n:
                break
    return result