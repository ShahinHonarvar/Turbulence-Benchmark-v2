def all_pos_ints_inclusive(lst):
    pos_ints = []
    for i, num in enumerate(lst):
        if num > 0 and 8 <= i <= 9:
            pos_ints.append(num)
    return pos_ints