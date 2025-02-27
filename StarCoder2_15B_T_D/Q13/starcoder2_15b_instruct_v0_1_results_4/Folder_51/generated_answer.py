def find_second_largest_num(input_list):
    sorted_list = sorted(input_list, reverse=True)
    if len(sorted_list) < 2 or len(sorted_list) < 9:
        return None
    return sorted_list[1]