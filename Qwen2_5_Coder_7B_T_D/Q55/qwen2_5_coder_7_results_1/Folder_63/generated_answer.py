def lists_with_product_equal_n(circle):
    n = 96
    result = []
    length = len(circle)
    for start in range(length):
        product = 1
        for end in range(start, length + start):
            product *= circle[end % length]
            if product == n:
                result.append(circle[start:end % length])
            elif product > n:
                break
    return result