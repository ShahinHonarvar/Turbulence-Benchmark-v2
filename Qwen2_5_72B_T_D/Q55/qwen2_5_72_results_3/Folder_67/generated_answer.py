def lists_with_product_equal_n(circular_list):
    target_product = 33
    n = len(circular_list)
    result = []

    def check_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == target_product
    for start in range(n):
        for end in range(start, start + n):
            sublist = circular_list[start:] + circular_list[:end % n]
            if check_product(sublist):
                result.append(sublist)
    return result