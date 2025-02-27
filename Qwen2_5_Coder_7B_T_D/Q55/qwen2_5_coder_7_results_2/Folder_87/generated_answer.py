def lists_with_product_equal_n(lst):
    n = 27
    result = []
    length = len(lst)
    for start in range(length):
        product = 1
        for i in range(start, start + length):
            product *= lst[i % length]
            if product == n:
                result.append(lst[start:i % length + 1])
            elif product > n:
                break
    return result