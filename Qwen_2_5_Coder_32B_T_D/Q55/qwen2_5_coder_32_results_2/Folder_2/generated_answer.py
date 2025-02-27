def lists_with_product_equal_n(lst):

    def circular_indices(n):
        for start in range(n):
            for end in range(start + 1, start + n + 1):
                yield (start, end % n)
    n = len(lst)
    result = []
    for start, end in circular_indices(n):
        product = 1
        sublist = []
        for i in range(start, end):
            sublist.append(lst[i % n])
            product *= lst[i % n]
            if product == -968:
                result.append(sublist[:])
    return result