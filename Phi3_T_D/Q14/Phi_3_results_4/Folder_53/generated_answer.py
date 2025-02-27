def find_second_smallest_num(lst):
    valid_range = lst[1:101]
    if len(valid_range) < 2:
        return None
    sorted_valid_range = sorted(valid_range)
    return sorted_valid_range[1]