def lists_with_product_equal_n(circular_list):
    result = []
    n = -57
    sublist_size = 1
    while sublist_size <= len(circular_list):
        for start_idx in range(len(circular_list)):
            product = 1
            for end_idx in range(start_idx, start_idx + sublist_size):
                product *= circular_list[end_idx % len(circular_list)]
                if product == n:
                    result.append(circular_list[start_idx:end_idx % len(circular_list) + 1])
        sublist_size += 1
    return result