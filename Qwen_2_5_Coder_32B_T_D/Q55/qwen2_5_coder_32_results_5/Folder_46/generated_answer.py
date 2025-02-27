def lists_with_product_equal_n(circular_list):
    n = 53
    result = []
    size = len(circular_list)
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= circular_list[end % size]
            if product == n:
                result.append(circular_list[start:(end + 1) % size] if start <= end else circular_list[start:] + circular_list[:end + 1])
            elif product > n:
                break
    return result