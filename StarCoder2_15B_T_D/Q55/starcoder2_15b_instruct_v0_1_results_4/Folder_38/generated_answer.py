def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    result = []
    for start in range(size):
        for length in range(1, size + 1):
            sublist = circular_list[start:start + length]
            if len(sublist) > size:
                sublist = sublist[:size]
            product = 1
            for num in sublist:
                product *= num
            if product == -23:
                result.append(sublist)
    return result