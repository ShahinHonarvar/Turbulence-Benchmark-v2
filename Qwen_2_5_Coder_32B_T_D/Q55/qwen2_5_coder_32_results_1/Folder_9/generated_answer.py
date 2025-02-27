def lists_with_product_equal_n(lst):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p
    n = len(lst)
    result = []
    for start in range(n):
        product_so_far = 1
        for end in range(start, start + n):
            product_so_far *= lst[end % n]
            if product_so_far == -36:
                result.append(lst[start % n:end % n + 1])
    return result