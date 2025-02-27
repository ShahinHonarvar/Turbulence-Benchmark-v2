def all_pos_ints_inclusive(int_list):
    start, end = (29, 79)
    pos_ints = [num for num in int_list[start:end + 1] if num > 0]
    return pos_ints