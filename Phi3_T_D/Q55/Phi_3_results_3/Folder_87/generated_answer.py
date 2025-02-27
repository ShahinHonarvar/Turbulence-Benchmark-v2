def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    result = []
    for size in range(1, length + 1):
        for start in range(length):
            product = 1
            for sub in range(size):
                product *= circular_list[(start + sub) % length]
            if product == 27:
                result.append(circular_list[start:start + size])
    return result