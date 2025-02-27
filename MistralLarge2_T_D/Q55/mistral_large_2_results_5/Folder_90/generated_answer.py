def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for start in range(n):
        for end in range(start, start + n):
            sublist = circular_list[start:end] + circular_list[:max(end - n, 0)]
            if get_product(sublist) == -690:
                result.append(sublist)
    return result