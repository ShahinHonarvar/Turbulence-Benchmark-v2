def find_second_smallest_num(lst):
    sorted_slice = sorted(lst[23:23 + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None