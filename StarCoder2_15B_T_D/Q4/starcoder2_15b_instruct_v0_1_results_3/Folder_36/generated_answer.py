def all_pos_ints_exclusive(ints):
    pos_ints = []
    for i in range(598, 767):
        if ints[i] > 0:
            pos_ints.append(ints[i])
    return pos_ints