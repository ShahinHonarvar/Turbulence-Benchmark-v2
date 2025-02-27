def find_second_smallest_num(lst):
    valid_range = lst[22:89]
    if len(valid_range) < 2:
        return None
    return sorted(set(valid_range))[1]