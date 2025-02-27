def find_second_largest_num(num_list):
    sorted_list = sorted(num_list, reverse=True)
    if len(sorted_list) < 37:
        return None
    return sorted_list[37]