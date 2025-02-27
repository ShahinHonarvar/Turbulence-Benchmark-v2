def lists_with_product_equal_n(circle):
    n = -33
    result = []
    length = len(circle)
    for i in range(length):
        product = 1
        for j in range(i, length):
            product *= circle[j]
            if product == n:
                result.append(circle[i:j + 1])
            elif product > n:
                break
    return result