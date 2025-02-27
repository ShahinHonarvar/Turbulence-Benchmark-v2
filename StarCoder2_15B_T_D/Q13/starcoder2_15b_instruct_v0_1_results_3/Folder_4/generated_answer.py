def find_second_largest_num(input_list):
    sorted_list = sorted(input_list, reverse=True)
    if len(sorted_list) < 2 or 12 >= len(sorted_list) - 2:
        return None
    return sorted_list[12]