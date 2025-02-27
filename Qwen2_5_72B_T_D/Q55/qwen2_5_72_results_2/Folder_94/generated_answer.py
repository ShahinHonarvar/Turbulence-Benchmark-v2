def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        for length in range(1, size + 1):
            index = (start + length - 1) % size
            product *= circular_list[index]
            if product == -30:
                result.append(circular_list[start:start + length] if start + length <= size else circular_list[start:] + circular_list[:length - size + start])
            elif abs(product) > 30:
                break
    return result