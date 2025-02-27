def find_second_smallest_num(num_list):
    if len(num_list[43:52]) < 2:
        return None
    sorted_slice = sorted(num_list[43:52])
    return sorted_slice[1]