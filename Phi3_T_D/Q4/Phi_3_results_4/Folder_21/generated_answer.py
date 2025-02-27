def all_pos_ints_exclusive(ints_list):
    start, end = (743, 867)
    return [num for num in ints_list[start:end] if num > 0]