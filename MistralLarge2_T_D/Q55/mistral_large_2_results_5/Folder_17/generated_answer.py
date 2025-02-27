def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j] + circular_list[:max(j - n, 0)]
            if product(sublist) == 18:
                result.append(sublist)
    return result