def all_pos_ints_inclusive(lst):
    pos_ints = []
    for i in range(8, 10):
        if lst[i] > 0:
            pos_ints.append(lst[i])
    return pos_ints