def lists_with_product_equal_n(lst):
    n = -51
    length = len(lst)
    result = []
    for i in range(length):
        product = 1
        for j in range(i, length):
            product *= lst[j % length]
            if product == n:
                result.append(lst[i:j + 1])
            elif product > abs(n):
                break
    return result