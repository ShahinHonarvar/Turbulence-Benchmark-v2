def all_pos_ints_exclusive(lst):
    pos_ints = []
    for i in range(len(lst)):
        if lst[i] > 0:
            pos_ints.append(lst[i])
    if len(pos_ints) >= 94:
        return pos_ints[93:94]
    else:
        return []