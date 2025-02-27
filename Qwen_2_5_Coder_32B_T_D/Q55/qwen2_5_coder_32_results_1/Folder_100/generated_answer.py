def lists_with_product_equal_n(circular_list):
    n = 48
    result = []
    size = len(circular_list)
    for i in range(size):
        product = 1
        for j in range(size):
            product *= circular_list[(i + j) % size]
            if product == n:
                result.append(circular_list[i:i + j + 1] if i + j + 1 <= size else circular_list[i:] + circular_list[:j + 1 - (size - i)])
            elif product > n:
                break
    return result