def lists_with_product_equal_n(lst):
    result = []
    n = -8
    length = len(lst)
    for start in range(length):
        product = 1
        for end in range(start, length):
            product *= lst[end]
            if product == n:
                result.append(lst[start:end + 1])
            elif product > n:
                break
    return result