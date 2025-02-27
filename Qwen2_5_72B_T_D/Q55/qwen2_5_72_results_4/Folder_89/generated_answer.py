def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        product = 1
        for number in lst:
            product *= number
        return product
    sublists = []
    n = len(circular_list)
    for start in range(n):
        for length in range(1, n + 1):
            sublist = circular_list[start:start + length] if start + length <= n else circular_list[start:] + circular_list[:length - (n - start)]
            if product_of_list(sublist) == 57:
                sublists.append(sublist)
    return sublists