def lists_with_product_equal_n(circular_list):
    n = -690
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        for end in range(size):
            idx = (start + end) % size
            product *= circular_list[idx]
            if product == n:
                result.append(circular_list[start:start + end + 1] if start + end < size else circular_list[start:] + circular_list[:idx + 1])
            elif product > n or (product < 0 and n > 0) or (product > 0 and n < 0):
                break
    return result