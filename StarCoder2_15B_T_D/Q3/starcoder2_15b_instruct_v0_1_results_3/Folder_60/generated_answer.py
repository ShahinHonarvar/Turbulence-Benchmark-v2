def all_pos_ints_inclusive(lst):
    pos_ints = [n for n in lst if n > 0]
    if len(pos_ints) < 11:
        return []
    return pos_ints[75:86]