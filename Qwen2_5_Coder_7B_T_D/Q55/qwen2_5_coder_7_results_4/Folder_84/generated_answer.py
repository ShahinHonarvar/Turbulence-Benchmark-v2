def lists_with_product_equal_n(l):
    n = -906
    length = len(l)
    result = []
    for i in range(length):
        product = 1
        for j in range(i, length):
            product *= l[j % length]
            if product == n:
                result.append(l[i:j + 1])
            elif product > n:
                break
    return result