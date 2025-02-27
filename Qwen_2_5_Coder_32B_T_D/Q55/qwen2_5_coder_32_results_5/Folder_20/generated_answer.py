def lists_with_product_equal_n(lst):
    n = -69
    result = []
    size = len(lst)
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            index = end % size
            product *= lst[index]
            if product == n:
                result.append(lst[start:index + 1])
    return result