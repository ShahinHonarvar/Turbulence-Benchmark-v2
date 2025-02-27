def all_pos_ints_inclusive(lst):
    pos_ints = []
    for i, num in enumerate(lst):
        if num > 0 and 56 <= i <= 82:
            pos_ints.append(num)
    return pos_ints