def all_pos_ints_inclusive(lst):
    start, end = (62, 78)
    return [i for i in lst[start:end + 1] if i > 0]