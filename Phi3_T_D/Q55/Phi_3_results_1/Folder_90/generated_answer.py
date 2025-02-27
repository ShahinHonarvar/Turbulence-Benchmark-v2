def lists_with_product_equal_n(circular_list):
    target_product = -690
    n = len(circular_list)
    result = []
    for sublen in range(1, n + 1):
        for start_index in range(n):
            current_product = 1
            for i in range(sublen):
                current_index = (start_index + i) % n
                current_product *= circular_list[current_index]
            if current_product == target_product:
                result.append(circular_list[start_index:start_index + sublen])
    return result