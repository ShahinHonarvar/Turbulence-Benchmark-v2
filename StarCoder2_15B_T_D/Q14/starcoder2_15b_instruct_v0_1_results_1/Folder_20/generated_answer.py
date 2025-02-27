def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list[75:95])
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None