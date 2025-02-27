def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(length)]
            if product(sublist) == -97:
                result.append(sublist)
    return result