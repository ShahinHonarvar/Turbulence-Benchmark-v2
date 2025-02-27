def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length) % n
            product *= lst[end]
            if product == -3:
                result.append(lst[start:end + 1] if start <= end else lst[start:] + lst[:end + 1])
            if product == 0:
                break
    return result