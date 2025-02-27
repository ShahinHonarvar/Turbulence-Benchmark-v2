def lists_with_product_equal_n(circular_list):
    n = 57
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for size in range(1, length + 1):
            end = (start + size) % length
            product *= circular_list[end - 1]
            if product == n:
                result.append(circular_list[start:end] if start < end else circular_list[start:] + circular_list[:end])
            if product != 0:
                product //= circular_list[(start + size - 1) % length]
    return result