def lists_with_product_equal_n(lst):
    n = 42
    result = []
    size = len(lst)
    for start in range(size):
        product = 1
        for length in range(1, size + 1):
            index = (start + length - 1) % size
            product *= lst[index]
            if product == n:
                result.append(lst[start:start + length])
            elif product > n:
                break
    return result