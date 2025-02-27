def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    if len(sorted_list) >= 23:
        return sorted_list[12 + 1]
    else:
        return None