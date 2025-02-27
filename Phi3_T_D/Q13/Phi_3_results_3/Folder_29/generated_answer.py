def find_second_largest_num(num_list):
    if len(num_list[59:98]) < 2:
        return None
    sorted_list = sorted(num_list[59:98])
    return sorted_list[-2]