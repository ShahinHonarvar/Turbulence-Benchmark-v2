def all_pos_ints_exclusive(integers):
    pos_ints = [x for index, x in enumerate(integers[1:3], start=1) if x > 0]
    return pos_ints