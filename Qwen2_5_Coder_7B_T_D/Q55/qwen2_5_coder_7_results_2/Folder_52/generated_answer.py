def lists_with_product_equal_n(lst):
    n = 37
    size = len(lst)
    result = []
    for start in range(size):
        current_product = 1
        for end in range(start, start + size):
            current_product *= lst[end % size]
            if current_product == n:
                result.append(lst[start:end % size + 1])
    return result