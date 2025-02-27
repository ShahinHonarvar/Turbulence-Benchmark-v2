def lists_with_product_equal_n(lst):
    n = 5
    result = []
    size = len(lst)
    for start in range(size):
        product = 1
        for i in range(start, size + start):
            product *= lst[i % size]
            if product == n:
                result.append(lst[start:i % size + 1])
            elif product > n:
                break
    return result