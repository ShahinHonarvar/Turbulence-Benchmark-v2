def all_pos_ints_exclusive(ints):
    pos_ints = []
    for i in ints:
        if i > 0:
            pos_ints.append(i)
    return pos_ints