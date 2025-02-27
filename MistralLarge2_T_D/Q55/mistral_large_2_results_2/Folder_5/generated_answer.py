def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    for start in range(n):
        for length in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(length)]
            if product(sublist) == -33:
                result.append(sublist)
    return result