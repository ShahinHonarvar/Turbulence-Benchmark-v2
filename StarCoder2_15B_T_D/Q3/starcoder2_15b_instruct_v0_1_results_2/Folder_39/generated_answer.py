def all_pos_ints_inclusive(lst):
    pos_ints = [i for i in lst if i > 0]
    if len(pos_ints) >= 20:
        return pos_ints[20:31]
    else:
        return []