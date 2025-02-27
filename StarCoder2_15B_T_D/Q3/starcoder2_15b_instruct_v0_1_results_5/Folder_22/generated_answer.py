def all_pos_ints_inclusive(lst):
    pos_ints = [x for x in lst if x > 0]
    return pos_ints[40:201] if len(pos_ints) >= 201 else []