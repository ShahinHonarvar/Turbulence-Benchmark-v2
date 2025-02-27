def all_pos_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if 0 < num and 0 < i < 9]