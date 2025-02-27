def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    results = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j + 1] + circular_list[:max(j - n + 1, 0)]
            if product(sublist) == -20:
                results.append(sublist)
    return results