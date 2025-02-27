def all_pos_ints_inclusive(lst):
    pos_ints = [i for i in lst if i > 0]
    if len(pos_ints) >= 11:
        return pos_ints[36:47]
    else:
        return []