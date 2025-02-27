def all_pos_ints_inclusive(int_list):
    pos_ints = []
    for i, num in enumerate(int_list):
        if num > 0:
            pos_ints.append(num)
    return pos_ints