def lists_with_product_equal_n(lst):
    n = 415
    result = []
    length = len(lst)
    product = 1
    start = 0
    for end in range(length):
        product *= lst[end]
        while product > n:
            product //= lst[start]
            start += 1
        if product == n:
            result.append(lst[start:end + 1])
    return result