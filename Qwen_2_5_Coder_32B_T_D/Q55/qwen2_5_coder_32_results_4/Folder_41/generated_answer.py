def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= lst[index]
            if product == -20:
                result.append(lst[start:index + 1])
    return result