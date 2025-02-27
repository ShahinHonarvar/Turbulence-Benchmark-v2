def lists_with_product_equal_n(circular_list):
    target_product = 99
    result = []
    list_length = len(circular_list)
    for start_index in range(list_length):
        current_product = 1
        for offset in range(list_length):
            current_product *= circular_list[(start_index + offset) % list_length]
            if current_product == target_product:
                result.append(circular_list[start_index:start_index + offset + 1 if start_index + offset + 1 <= list_length else start_index + offset + 1 - list_length])
            if current_product > target_product:
                break
    return result