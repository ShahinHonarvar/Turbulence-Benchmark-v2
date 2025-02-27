def lists_with_product_equal_n(lst):

    def product_of_list(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start + 1, n + 1):
            current_sublist = lst[start:end] if end != n else lst[start:] + lst[:end - n]
            if product_of_list(current_sublist) == -72:
                result.append(current_sublist)
    return result