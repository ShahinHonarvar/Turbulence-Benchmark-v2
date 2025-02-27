def all_pos_ints_exclusive(lst):
    if len(lst) < 99:
        return []
    pos_ints = []
    for i in range(15, 99):
        if lst[i] > 0:
            pos_ints.append(lst[i])
    return pos_ints