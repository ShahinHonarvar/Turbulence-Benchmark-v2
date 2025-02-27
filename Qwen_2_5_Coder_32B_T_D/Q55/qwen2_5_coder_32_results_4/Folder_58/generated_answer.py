def lists_with_product_equal_n(circular_list):
    n = 733
    result = []
    size = len(circular_list)
    for start in range(size):
        product = 1
        for i in range(start, start + size):
            product *= circular_list[i % size]
            if product == n:
                result.append(circular_list[start:(i + 1) % size])
            elif product > n:
                break
    return result