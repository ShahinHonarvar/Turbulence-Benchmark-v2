def lists_with_product_equal_n(circular_list):
    n = -75
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for size in range(1, length + 1):
            end = (start + size) % length
            product *= circular_list[end]
            if product == n:
                result.append(circular_list[start:end])
    return result