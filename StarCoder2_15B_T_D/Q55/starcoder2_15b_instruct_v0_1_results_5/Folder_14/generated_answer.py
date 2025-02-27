def lists_with_product_equal_n(lst):
    result = []
    n = -72
    product = 1
    start = 0
    for i, num in enumerate(lst):
        product *= num
        while product > n:
            product //= lst[start]
            start += 1
        if product == n:
            result.append(lst[start:i + 1])
    return result