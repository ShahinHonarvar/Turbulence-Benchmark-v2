def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            end %= n
            product *= lst[end]
            if product == -16:
                result.append(lst[start:end + 1])
    return result