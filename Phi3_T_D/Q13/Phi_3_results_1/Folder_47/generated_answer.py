def find_second_largest_num(input_list):
    sliced_list = input_list[37:77]
    if len(sliced_list) < 2 or len(set(sliced_list)) < 2:
        return None
    sliced_list_sorted = sorted(sliced_list, reverse=True)
    return sliced_list_sorted[1]