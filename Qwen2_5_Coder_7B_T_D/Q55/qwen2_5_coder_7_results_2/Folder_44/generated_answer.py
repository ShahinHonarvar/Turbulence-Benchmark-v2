def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product = 1
    start = 0
    for end in range(n):
        product *= lst[end]
        while product % 29 == 0:
            if product == 29:
                result.append(lst[start:end + 1])
            product //= lst[start]
            start += 1
    return result