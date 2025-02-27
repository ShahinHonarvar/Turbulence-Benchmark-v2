def lists_with_product_equal_n(lst):
    n = -54
    result = []
    length = len(lst)
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            index = end % length
            product *= lst[index]
            if product == n:
                sublist = lst[start:index + 1] if start <= index else lst[start:] + lst[:index + 1]
                result.append(sublist)
            if product == 0:
                break
    return result