def all_pos_ints_inclusive(lst):
    start_index, end_index = (19, 92)
    return [item for item in lst[start_index:end_index + 1] if item > 0]