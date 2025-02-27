def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start_index in range(n):
        current_product = 1
        for sublist_size in range(1, n + 1):
            end_index = (start_index + sublist_size) % n
            if end_index == start_index:
                break
            current_product *= circular_list[end_index]
            if current_product == -72:
                result.append(circular_list[start_index:end_index + 1])
            if abs(current_product) > 72:
                break
    return result