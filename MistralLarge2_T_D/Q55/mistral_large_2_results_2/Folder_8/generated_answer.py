def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        for length in range(1, size + 1):
            end = (start + length) % size
            product *= circular_list[end]
            if product == -41:
                sublist = [circular_list[(start + i) % size] for i in range(length + 1)]
                result.append(sublist)
    return result