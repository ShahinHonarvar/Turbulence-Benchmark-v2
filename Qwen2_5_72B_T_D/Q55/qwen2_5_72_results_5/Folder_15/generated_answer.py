def lists_with_product_equal_n(circular_list):

    def check_product(sublist, target=-7):
        product = 1
        for num in sublist:
            product *= num
        return product == target
    size = len(circular_list)
    result = []
    for start in range(size):
        for length in range(1, size + 1):
            sublist = circular_list[start:start + length]
            if len(sublist) < length:
                sublist += circular_list[:length - len(sublist)]
            if check_product(sublist):
                result.append(sublist)
    return result