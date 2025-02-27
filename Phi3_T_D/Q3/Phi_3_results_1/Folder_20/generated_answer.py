def all_pos_ints_inclusive(lst):
    start, end = (56, 66)
    return [x for x in lst[start:end + 1] if x > 0]