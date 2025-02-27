def lists_with_product_equal_n(lst):
    result = []
    n = 57
    length = len(lst)
    for start in range(length):
        product = 1
        for i in range(length):
            product *= lst[(start + i) % length]
            if product == n:
                result.append(lst[start:start + i + 1])
            elif product > n:
                break
    return result