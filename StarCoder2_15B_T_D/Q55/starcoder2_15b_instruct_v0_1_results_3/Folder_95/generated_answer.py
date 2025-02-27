def lists_with_product_equal_n(lst, n):
    result = []
    product = 1
    start = 0
    end = 0
    while end < len(lst):
        product *= lst[end]
        while product > n:
            product /= lst[start]
            start += 1
        if product == n:
            result.append(lst[start:end + 1])
        end += 1
    return result