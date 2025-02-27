def lists_with_product_equal_n(circular_list):
    target_product = -968
    n = len(circular_list)
    result = []

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    for i in range(n):
        for j in range(1, n + 1):
            sublist = circular_list[i:i + j] + circular_list[:j - (n - i)]
            if product(sublist) == target_product:
                result.append(sublist)
    return result