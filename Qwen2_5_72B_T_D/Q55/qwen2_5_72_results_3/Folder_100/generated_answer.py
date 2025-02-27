def lists_with_product_equal_n(circular_list):
    target_product = 48
    n = len(circular_list)
    result = []
    for start in range(n):
        current_product = 1
        for size in range(1, n + 1):
            end = (start + size) % n
            current_product *= circular_list[end - 1]
            if current_product == target_product:
                result.append(circular_list[start:end] if start < end else circular_list[start:] + circular_list[:end])
            if current_product > target_product:
                break
        current_product //= circular_list[start]
    return result