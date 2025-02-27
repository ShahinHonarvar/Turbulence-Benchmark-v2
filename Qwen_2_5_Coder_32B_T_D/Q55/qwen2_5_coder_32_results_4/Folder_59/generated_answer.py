def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= lst[index]
            if product == -3:
                result.append(lst[start:end + 1] if end < start + n else lst[start:] + lst[:end % n + 1])
    return result