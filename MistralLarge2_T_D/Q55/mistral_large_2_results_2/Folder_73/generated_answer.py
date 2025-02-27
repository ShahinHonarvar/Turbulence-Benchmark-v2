def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length) % n
            product *= circular_list[end]
            if product == 40:
                result.append(circular_list[start:end + 1] if start <= end else circular_list[start:] + circular_list[:end + 1])
            elif product > 40:
                break
    return result