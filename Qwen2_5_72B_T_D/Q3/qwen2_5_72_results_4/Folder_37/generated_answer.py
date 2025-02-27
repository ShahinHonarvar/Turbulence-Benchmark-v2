def all_pos_ints_inclusive(lst):
    return [num for i, num in enumerate(lst[1:6], start=1) if num > 0]