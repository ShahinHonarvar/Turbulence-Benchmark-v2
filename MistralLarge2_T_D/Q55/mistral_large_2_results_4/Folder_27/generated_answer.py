def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            sublist = circular_list[i:j]
            if len(sublist) > n:
                break
            if product(sublist) == -82:
                result.append(sublist)
    return result