def lists_with_product_equal_n(circular_list, n):
    result = []
    for start_index in range(len(circular_list)):
        current_product = 1
        current_list = []
        for i in range(start_index, start_index + len(circular_list)):
            current_index = i % len(circular_list)
            current_product *= circular_list[current_index]
            current_list.append(circular_list[current_index])
            if current_product == n:
                result.append(current_list)
            elif current_product > n:
                break
    return result