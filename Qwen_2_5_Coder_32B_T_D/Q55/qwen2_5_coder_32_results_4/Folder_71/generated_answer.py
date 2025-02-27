def lists_with_product_equal_n(lst):
    n = 47
    result = []
    size = len(lst)
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            index = end % size
            product *= lst[index]
            if product == n:
                result.append(lst[start:index + 1])
            elif product > n:
                break
    return result