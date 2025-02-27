def find_second_smallest_num(lst):
    if len(lst[43:52]) < 2:
        return None
    sorted_slice = sorted(lst[43:52])
    return sorted_slice[1]