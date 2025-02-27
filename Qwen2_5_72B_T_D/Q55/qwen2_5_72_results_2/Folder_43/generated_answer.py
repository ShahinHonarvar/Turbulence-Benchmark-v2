def lists_with_product_equal_n(circular_list):

    def check_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == -26
    size = len(circular_list)
    result = []
    for start in range(size):
        for end in range(1, size + 1):
            sublist = circular_list[start:] + circular_list[:end]
            if check_product(sublist):
                result.append(sublist)
    return result