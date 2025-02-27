def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    if len(sorted_list) >= 4:
        return sorted_list[4]
    else:
        return None