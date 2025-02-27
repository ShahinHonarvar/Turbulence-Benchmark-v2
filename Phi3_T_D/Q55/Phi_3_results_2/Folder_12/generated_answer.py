def lists_with_product_equal_n(circular_list):
    target_product = 18
    valid_sublists = []
    list_length = len(circular_list)
    if list_length == 0:
        return valid_sublists

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result

    def find_sublists(start_index, current_list):
        if start_index == list_length:
            start_index = 0
        for end_index in range(start_index, len(circular_list)):
            current_sublist = current_list + [circular_list[end_index]]
            if product(current_sublist) == target_product:
                valid_sublists.append(current_sublist)
            find_sublists(start_index + 1, current_sublist)
    find_sublists(0, [])
    return valid_sublists