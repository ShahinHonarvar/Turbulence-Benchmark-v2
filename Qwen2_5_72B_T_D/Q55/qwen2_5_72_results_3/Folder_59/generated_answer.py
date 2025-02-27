def lists_with_product_equal_n(circular_list):

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    size = len(circular_list)
    result = []
    for start in range(size):
        for length in range(1, size + 1):
            if length <= size:
                sublist = circular_list[start:start + length]
                if start + length > size:
                    sublist = circular_list[start:] + circular_list[:start + length - size]
                if product_of_sublist(sublist) == -3:
                    result.append(sublist)
    return result