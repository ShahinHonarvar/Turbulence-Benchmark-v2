def lists_with_product_equal_n(lst):

    def product_of_list(sublst):
        product = 1
        for num in sublst:
            product *= num
        return product
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = lst[start:end % n]
            if product_of_list(sublist) == -95:
                result.append(sublist)
    return result