def lists_with_product_equal_n(circular_list):
    n = 49
    size = len(circular_list)
    result = []
    for i in range(size):
        product = 1
        for j in range(size):
            product *= circular_list[(i + j) % size]
            if product == n:
                result.append(circular_list[i:i + j + 1] + circular_list[:i + j + 1 - size])
            elif product > n:
                break
    return result