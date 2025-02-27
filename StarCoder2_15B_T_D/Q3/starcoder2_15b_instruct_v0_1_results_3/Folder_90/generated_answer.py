def all_pos_ints_inclusive(lst):
    pos_ints = [x for x in lst if x > 0]
    return pos_ints[262:747] if len(pos_ints) >= 485 else []