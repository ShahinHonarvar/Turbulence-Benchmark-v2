def lists_with_product_equal_n(circular_list):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = circular_list[start:] + circular_list[:end % n]
            if product(sublist) == 40:
                result.append(sublist)
    return result