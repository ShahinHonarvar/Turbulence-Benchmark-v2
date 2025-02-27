def find_second_largest_num(input_list):
    sorted_list = sorted(input_list, reverse=True)
    if len(sorted_list) >= 33:
        return sorted_list[28]
    else:
        return None