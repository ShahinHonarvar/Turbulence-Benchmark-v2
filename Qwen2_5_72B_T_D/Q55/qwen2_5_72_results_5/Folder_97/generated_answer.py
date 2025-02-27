def lists_with_product_equal_n(circular_list):
    target_product = -938
    list_length = len(circular_list)
    valid_sublists = []

    def find_sublists(start_index, current_product, current_sublist):
        if current_product == target_product:
            valid_sublists.append(current_sublist.copy())
        if current_product != 0 and target_product % current_product == 0:
            for i in range(1, list_length + 1):
                next_index = (start_index + i) % list_length
                next_value = circular_list[next_index]
                find_sublists(next_index, current_product * next_value, current_sublist + [next_value])
    for i in range(list_length):
        find_sublists(i, 1, [])
    return valid_sublists