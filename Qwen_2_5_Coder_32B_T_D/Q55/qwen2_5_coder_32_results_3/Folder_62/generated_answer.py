def lists_with_product_equal_n(lst):

    def product(sub):
        p = 1
        for num in sub:
            p *= num
        return p
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sub = lst[start:end]
            if product(sub) == 100:
                result.append(sub)
    return result