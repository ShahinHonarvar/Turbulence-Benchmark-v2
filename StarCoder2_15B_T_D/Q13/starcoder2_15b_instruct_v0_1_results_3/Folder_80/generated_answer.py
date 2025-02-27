def find_second_largest_num(input_list):
    sorted_list = sorted(input_list, reverse=True)
    if len(sorted_list) >= 66:
        return sorted_list[65]
    else:
        return None