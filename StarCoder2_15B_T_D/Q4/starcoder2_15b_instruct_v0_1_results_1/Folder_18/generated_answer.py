def all_pos_ints_exclusive(lst):
    pos_ints = []
    for i, num in enumerate(lst):
        if num > 0 and 57 < i < 84:
            pos_ints.append(num)
    return pos_ints