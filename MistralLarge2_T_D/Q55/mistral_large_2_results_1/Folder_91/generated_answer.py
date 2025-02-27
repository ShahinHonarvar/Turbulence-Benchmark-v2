def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        current_product = 1
        for length in range(1, n + 1):
            current_product *= circular_list[(start + length - 1) % n]
            if current_product == 2:
                result.append(circular_list[start:start + length])
            elif current_product > 2:
                break
    return result