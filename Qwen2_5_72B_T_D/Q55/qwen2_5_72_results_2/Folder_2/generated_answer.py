def lists_with_product_equal_n(circular_list):

    def product_of_sublist(sublist):
        result = 1
        for number in sublist:
            result *= number
        return result
    n = len(circular_list)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            sublist = circular_list[start:start + size] or circular_list[start:] + circular_list[:size - (n - start)]
            if product_of_sublist(sublist) == -968:
                result.append(sublist)
    return result