def lists_with_product_equal_n(circular_list):
    n = -91
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        for end in range(size):
            current_index = (start + end) % size
            product *= circular_list[current_index]
            if product == n:
                result.append(circular_list[start:current_index + 1])
            elif abs(product) > n:
                break
    return result