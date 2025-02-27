def lists_with_product_equal_n(lst):
    n = -44
    result = []
    size = len(lst)
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= lst[end % size]
            if product == n:
                result.append(lst[start:(end + 1) % size] if (end + 1) % size != start else lst[start:])
    return result