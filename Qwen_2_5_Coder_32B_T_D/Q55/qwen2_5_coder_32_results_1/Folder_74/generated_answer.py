def lists_with_product_equal_n(lst):

    def product(sub):
        p = 1
        for n in sub:
            p *= n
        return p
    n = len(lst)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            sublist = [lst[(start + i) % n] for i in range(size)]
            if product(sublist) == 51:
                result.append(sublist)
    return result