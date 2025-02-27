def find_second_largest_num(input_list):
    sorted_list = sorted(input_list, reverse=True)
    if len(sorted_list) < 2 or 93 - 29 + 1 < 2:
        return None
    return sorted_list[29:94][1]