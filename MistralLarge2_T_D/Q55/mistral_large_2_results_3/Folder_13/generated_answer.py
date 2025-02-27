def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def product(sublist):
        p = 1
        for x in sublist:
            p *= x
        return p
    for start in range(n):
        for length in range(1, n + 1):
            sublist = circular_list[start:start + length]
            if len(sublist) < n:
                sublist += circular_list[:max(0, length - (n - start))]
            if product(sublist) == 54:
                result.append(sublist)
    return result