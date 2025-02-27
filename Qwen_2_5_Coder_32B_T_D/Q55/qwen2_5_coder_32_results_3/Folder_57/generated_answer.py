def lists_with_product_equal_n(lst):
    n = -75
    result = []
    size = len(lst)
    for start in range(size):
        product = 1
        for i in range(size):
            index = (start + i) % size
            product *= lst[index]
            if product == n:
                result.append(lst[start:index + 1])
    return result