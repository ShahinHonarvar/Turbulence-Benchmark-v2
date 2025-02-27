def all_pos_ints_exclusive(input_list):
    if len(input_list) < 82:
        return []
    else:
        filtered_list = [x for x in input_list[38:81] if x > 0]
        return filtered_list