def lists_with_product_equal_n(circular_list):

    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = circular_list[start:end % n]
            if get_product(sublist) == 100:
                result.append(sublist)
    return result