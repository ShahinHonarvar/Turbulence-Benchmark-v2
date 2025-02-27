def lists_with_product_equal_n(lst):
    n = 46
    length = len(lst)
    result = []
    for start in range(length):
        product = 1
        for end in range(start, length):
            product *= lst[end]
            if product == n:
                result.append(lst[start:end + 1])
    return result