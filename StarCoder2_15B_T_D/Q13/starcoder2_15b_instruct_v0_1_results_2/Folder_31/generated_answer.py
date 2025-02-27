def find_second_largest_num(input_list):
    sorted_list = sorted(input_list)
    if len(sorted_list) > 1:
        return sorted_list[-2]
    else:
        return None