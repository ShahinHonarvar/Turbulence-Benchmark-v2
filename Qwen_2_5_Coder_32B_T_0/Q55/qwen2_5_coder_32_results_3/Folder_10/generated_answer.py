def lists_with_product_equal_n(lst):
    n = -93
    result = []
    length = len(lst)
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= lst[end % length]
            if product == n:
                result.append(lst[start:end % length + 1])
    return result