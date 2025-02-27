def all_pos_ints_inclusive(ints):
    pos_ints = []
    for i, num in enumerate(ints):
        if num > 0 and 25 <= i <= 59:
            pos_ints.append(num)
    return pos_ints