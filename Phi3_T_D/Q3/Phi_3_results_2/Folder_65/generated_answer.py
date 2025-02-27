def all_pos_ints_inclusive(lst):
    start = 56
    end = 98
    return [x for x in lst[start:end + 1] if x > 0]