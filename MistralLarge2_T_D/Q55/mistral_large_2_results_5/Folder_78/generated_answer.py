def lists_with_product_equal_n(circular_list):
    n = 74
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        for end in range(size):
            product *= circular_list[(start + end) % size]
            if product == n:
                result.append(circular_list[start:start + end + 1])
            elif product > n:
                break
    return result