def all_pos_ints_exclusive(lst):
    pos_ints = []
    for i, num in enumerate(lst):
        if num > 0 and 18 < i < 60:
            pos_ints.append(num)
    return pos_ints