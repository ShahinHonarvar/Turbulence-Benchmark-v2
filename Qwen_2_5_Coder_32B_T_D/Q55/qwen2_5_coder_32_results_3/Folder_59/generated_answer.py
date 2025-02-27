def lists_with_product_equal_n(lst):

    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            current_sublist = lst[start:end % n]
            if get_product(current_sublist) == -3:
                result.append(current_sublist)
    return result