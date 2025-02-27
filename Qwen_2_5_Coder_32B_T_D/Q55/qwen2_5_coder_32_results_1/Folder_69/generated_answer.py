def lists_with_product_equal_n(lst):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            if product([lst[(start + i) % n] for i in range(end)]) == 90:
                result.append([lst[(start + i) % n] for i in range(end)])
    return result