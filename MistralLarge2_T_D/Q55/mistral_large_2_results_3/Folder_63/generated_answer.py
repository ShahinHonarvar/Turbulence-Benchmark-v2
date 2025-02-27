def lists_with_product_equal_n(circular_list):
    n = 96
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for size in range(1, length + 1):
            end = (start + size) % length
            product *= circular_list[end]
            if product == n:
                result.append(circular_list[start:end + 1] if end >= start else circular_list[start:] + circular_list[:end + 1])
            elif product > n:
                break
    return result