def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            end_index = end % n
            product *= lst[end_index]
            if product == -690:
                result.append(lst[start:end_index + 1])
    return result