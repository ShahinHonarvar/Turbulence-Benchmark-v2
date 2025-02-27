def all_pos_ints_exclusive(integers_list):
    pos_ints = []
    for i, num in enumerate(integers_list):
        if num > 0 and 38 < i < 52:
            pos_ints.append(num)
    return pos_ints