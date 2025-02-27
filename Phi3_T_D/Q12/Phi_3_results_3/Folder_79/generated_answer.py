def find_smallest_num(num_list):
    if len(num_list) < 6:
        raise ValueError('The input list must have at least 6 elements.')
    return min(num_list[1:6])