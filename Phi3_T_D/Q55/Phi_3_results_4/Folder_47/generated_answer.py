def lists_with_product_equal_n(circular_list):
    num_elements = len(circular_list)
    found_sublists = []
    for start_index in range(num_elements):
        product = 1
        for sublist_length in range(1, num_elements + 1):
            temp_product = 1
            for i in range(start_index, start_index + sublist_length):
                temp_product *= circular_list[i % num_elements]
            if temp_product == -94:
                found_sublists.append(circular_list[start_index:start_index + sublist_length])
    return found_sublists