def lists_with_product_equal_n(circular_list):

    def product(lst):
        prod = 1
        for x in lst:
            prod *= x
        return prod
    n = len(circular_list)
    results = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(length)]
            if product(sublist) == 36:
                results.append(sublist)
    return results