def all_pos_ints_exclusive(lst):
    pos_ints = [x for x in lst if x > 0]
    if len(pos_ints) >= 86:
        return pos_ints[81:86]
    else:
        return []