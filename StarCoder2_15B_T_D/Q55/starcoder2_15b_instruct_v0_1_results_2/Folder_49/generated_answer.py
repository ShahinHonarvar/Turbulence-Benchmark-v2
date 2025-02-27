def lists_with_product_equal_n(circular_list):
    result = []
    for start_index in range(len(circular_list)):
        current_product = 1
        current_list = []
        for i in range(start_index, start_index + len(circular_list)):
            current_product *= circular_list[i % len(circular_list)]
            current_list.append(circular_list[i % len(circular_list)])
            if current_product == -61:
                result.append(current_list[:])
            if current_product == 0:
                break
    return result