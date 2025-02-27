def lists_with_product_equal_n(circular_list):
    target_product = 537
    size = len(circular_list)
    n = size // 2

    def is_valid_sublist_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == target_product
    result = []
    for length in range(1, n + 1):
        for start in range(size):
            sublist = circular_list[start:start + length]
            if is_valid_sublist_product(sublist):
                result.append(sublist)
            if start + length == size:
                wrapped_sublist = circular_list[length:] + circular_list[:length]
                if is_valid_sublist_product(wrapped_sublist):
                    result.append(wrapped_sublist)
    return result