def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def product(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j + 1]
            if product(sublist) == -20:
                result.append(sublist)
    return result