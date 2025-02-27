def all_pos_ints_inclusive(lst):
    if len(lst) < 72:
        return []
    pos_ints = []
    for i in range(52, 72):
        if lst[i] > 0:
            pos_ints.append(lst[i])
    return pos_ints