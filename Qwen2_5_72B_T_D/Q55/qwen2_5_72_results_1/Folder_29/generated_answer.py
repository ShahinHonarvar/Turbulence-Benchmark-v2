def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    size = len(circular_list)
    result = []
    for start in range(size):
        for length in range(1, size + 1):
            sublist = circular_list[start:start + length] + circular_list[:max(0, length - size + start)]
            if product_of_list(sublist) == 15:
                result.append(sublist)
    return result