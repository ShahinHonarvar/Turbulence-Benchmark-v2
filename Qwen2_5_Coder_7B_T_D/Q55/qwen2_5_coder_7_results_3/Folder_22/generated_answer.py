def lists_with_product_equal_n(lst):

    def is_product_of_sublist(sublist, n):
        product = 1
        for num in sublist:
            product *= num
        return product == n
    n = 4
    result = []
    lst_len = len(lst)
    for start in range(lst_len):
        for end in range(start + 1, lst_len + 1):
            sublist = lst[start:end] + lst[:start]
            if is_product_of_sublist(sublist, n):
                result.append(sublist)
    return result