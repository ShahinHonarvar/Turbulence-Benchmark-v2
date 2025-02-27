def lists_with_product_equal_n(lst):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            sublist = [lst[(i + k) % n] for k in range(j)]
            if product(sublist) == -906:
                result.append(sublist)
    return result