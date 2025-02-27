def lists_with_product_equal_n(circular_list, n):
    result = []
    circular_list_len = len(circular_list)
    for start_index in range(circular_list_len):
        current_product = 1
        current_list = []
        for i in range(start_index, start_index + circular_list_len):
            current_index = i % circular_list_len
            current_element = circular_list[current_index]
            current_product *= current_element
            current_list.append(current_element)
            if current_product == n:
                result.append(current_list[:])
            elif current_product == 0:
                break
    return result