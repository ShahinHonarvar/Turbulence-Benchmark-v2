def lists_with_product_equal_n(lst):
    n = 91
    result = []
    size = len(lst)
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= lst[end % size]
            if product == n:
                result.append(lst[start:end % size + 1])
            if product == 0 or product % n != 0:
                break
    return result