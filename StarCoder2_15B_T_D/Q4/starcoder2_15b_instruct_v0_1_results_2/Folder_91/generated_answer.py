def all_pos_ints_exclusive(ints):
    pos_ints = []
    for i in range(len(ints)):
        if i < 0 or i >= 5:
            continue
        if ints[i] > 0:
            pos_ints.append(ints[i])
    return pos_ints