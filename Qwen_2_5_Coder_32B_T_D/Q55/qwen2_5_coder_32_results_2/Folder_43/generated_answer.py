def lists_with_product_equal_n(lst):
    n = -26
    result = []
    length = len(lst)
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            index = end % length
            product *= lst[index]
            if product == n:
                result.append(lst[start:index + 1])
    return result