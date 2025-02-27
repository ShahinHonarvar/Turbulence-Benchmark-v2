def all_pos_ints_exclusive(num_list):
    pos_ints = []
    for i, num in enumerate(num_list):
        if num > 0:
            pos_ints.append(num)
    return pos_ints