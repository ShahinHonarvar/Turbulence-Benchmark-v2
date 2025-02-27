def all_pos_ints_exclusive(int_list):
    pos_ints = []
    for i, num in enumerate(int_list):
        if 44 < i < 67 and num > 0:
            pos_ints.append(num)
    return pos_ints