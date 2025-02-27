def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)
    for start_index in range(size):
        for length in range(1, size + 1):
            sublist = circular_list[start_index:start_index + length]
            if len(sublist) > size:
                sublist = sublist[:size]
            product = 1
            for num in sublist:
                product *= num
            if product == -57:
                result.append(sublist)
    return result