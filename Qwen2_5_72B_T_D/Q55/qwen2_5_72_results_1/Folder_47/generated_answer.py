def lists_with_product_equal_n(circular_list):
    target_product = -94
    size = len(circular_list)
    result = []
    for start in range(size):
        for end in range(1, size + 1):
            sublist = circular_list[start:] + circular_list[:end]
            product = 1
            for num in sublist:
                product *= num
            if product == target_product:
                result.append(sublist)
    return result