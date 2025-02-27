def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= lst[index]
            if product == 93:
                result.append(lst[start:index + 1])
            elif product > 93:
                break
    return result