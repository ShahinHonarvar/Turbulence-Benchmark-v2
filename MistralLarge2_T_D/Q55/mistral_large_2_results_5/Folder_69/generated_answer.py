def lists_with_product_equal_n(circular_list):

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    n = len(circular_list)
    result = []
    for length in range(1, n + 1):
        for start in range(n):
            sublist = [circular_list[(start + i) % n] for i in range(length)]
            if product(sublist) == 90:
                result.append(sublist)
    return result