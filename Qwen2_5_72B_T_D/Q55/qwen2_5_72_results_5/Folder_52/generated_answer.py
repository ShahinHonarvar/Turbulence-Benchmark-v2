def lists_with_product_equal_n(circular_list):
    n = 37
    length = len(circular_list)
    result = []
    for start in range(length):
        for size in range(1, length + 1):
            product = 1
            for j in range(size):
                product *= circular_list[(start + j) % length]
            if product == n:
                result.append(circular_list[start:(start + size) % length] if (start + size) % length > start else circular_list[start:] + circular_list[:size - (length - start)])
    return result