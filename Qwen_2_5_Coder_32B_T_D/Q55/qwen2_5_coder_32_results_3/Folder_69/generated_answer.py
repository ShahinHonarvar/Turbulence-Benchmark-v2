def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= lst[end % n]
            if product == 90:
                result.append(lst[start:(end + 1) % n] if start <= end else lst[start:] + lst[:end + 1])
            elif product > 90:
                break
    return result