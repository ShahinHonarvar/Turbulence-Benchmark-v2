def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    if len(sorted_list) >= 2 and 6 < len(sorted_list):
        return sorted_list[6]
    else:
        return None