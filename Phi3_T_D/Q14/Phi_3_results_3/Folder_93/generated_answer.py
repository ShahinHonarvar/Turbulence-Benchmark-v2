def find_second_smallest_num(num_list):
    if len(num_list) < 14 or len(num_list[75:89]) < 2:
        return None
    sorted_slice = sorted(num_list[75:89])
    return sorted_slice[1]