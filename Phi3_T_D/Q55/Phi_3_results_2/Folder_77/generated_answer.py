def lists_with_product_equal_n(circular):
    result = []
    len_circular = len(circular)

    def is_product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 632
    for window_size in range(1, len_circular + 1):
        for start in range(len_circular):
            end = (start + window_size) % len_circular
            if end == 0:
                portion = circular[start:] + circular[:start]
            else:
                portion = circular[start:end]
            if is_product_equal_n(portion):
                result.append(portion)
    return result