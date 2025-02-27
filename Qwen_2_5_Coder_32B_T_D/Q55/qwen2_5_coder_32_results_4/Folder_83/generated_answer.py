def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            index = (start + size - 1) % n
            product *= lst[index]
            if product == -57:
                result.append(lst[start:index + 1] if start <= index else lst[start:] + lst[:index + 1])
    return result