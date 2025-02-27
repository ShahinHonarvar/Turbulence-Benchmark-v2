def lists_with_product_equal_n(circular_list):

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = circular_list[start:start + length] or circular_list[start:] + circular_list[:length - (n - start)]
            if product_of_sublist(sublist) == -18:
                result.append(sublist)
    return result