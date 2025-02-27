def lists_with_product_equal_n(circular_list, n=-46):
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for size in range(1, length + 1):
            product *= circular_list[(start + size - 1) % length]
            if product == n:
                result.append(circular_list[start:start + size])
    return result