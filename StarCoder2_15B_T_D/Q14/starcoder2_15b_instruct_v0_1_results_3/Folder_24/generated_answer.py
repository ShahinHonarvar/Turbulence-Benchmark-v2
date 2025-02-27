def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    if len(sorted_list) >= 24:
        return sorted_list[23]
    else:
        return None