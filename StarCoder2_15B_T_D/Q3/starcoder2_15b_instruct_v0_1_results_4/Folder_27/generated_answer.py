def all_pos_ints_inclusive(int_list):
    pos_ints = []
    for idx, num in enumerate(int_list):
        if num > 0 and idx >= 66 and (idx <= 93):
            pos_ints.append(num)
    return pos_ints