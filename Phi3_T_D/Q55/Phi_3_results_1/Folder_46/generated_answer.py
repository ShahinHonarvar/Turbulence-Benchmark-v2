def lists_with_product_equal_n(circular_list):
    target_product = 53
    n = len(circular_list)
    result = []
    for start in range(n):
        current_product = 1
        for end in range(start, n + start):
            current_product *= circular_list[end % n]
            if current_product == target_product:
                result.append(circular_list[start:end % n + 1])
            elif current_product > target_product:
                break
    return result