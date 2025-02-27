def lists_with_product_equal_n(circle):
    n = 78
    result = []
    length = len(circle)
    for i in range(length):
        product = 1
        for j in range(i, length + i):
            product *= circle[j % length]
            if product == n:
                result.append(circle[i:j % length])
    return result