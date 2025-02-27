def lists_with_product_equal_n(circ_list):

    def product(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod
    n = len(circ_list)
    results = []
    for start in range(n):
        current = []
        for i in range(n):
            current.append(circ_list[(start + i) % n])
            if product(current) == 51:
                results.append(current[:])
    return results