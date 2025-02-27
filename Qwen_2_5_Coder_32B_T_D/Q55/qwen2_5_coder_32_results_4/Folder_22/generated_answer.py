def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= lst[index]
            if product == 4:
                result.append(lst[start:index + 1])
            elif product > 4:
                break
    return result