def all_pos_ints_exclusive(lst):
    pos_ints = []
    for i, num in enumerate(lst):
        if 8 <= i < 9 and num > 0:
            pos_ints.append(num)
    return pos_ints