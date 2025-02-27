def lists_with_product_equal_n(lst):

    def circular_sublists(lst):
        n = len(lst)
        for start in range(n):
            for end in range(start + 1, start + n + 1):
                yield (lst[start:end % n] if start <= end % n else lst[start:] + lst[:end % n])
    result = []
    for sub in circular_sublists(lst):
        prod = 1
        for num in sub:
            prod *= num
        if prod == 49:
            result.append(sub)
    return result