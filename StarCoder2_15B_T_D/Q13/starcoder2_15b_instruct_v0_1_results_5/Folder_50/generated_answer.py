def find_second_largest_num(input_list):
    sorted_list = sorted(input_list, reverse=True)
    if len(sorted_list) < 85:
        return None
    return sorted_list[70]