def lists_with_product_equal_n(lst):
    n = -26
    result = []
    length = len(lst)
    for start in range(length):
        product = 1
        for i in range(start, length + start):
            product *= lst[i % length]
            if product == n:
                result.append(lst[start:i % length + 1])
    return result