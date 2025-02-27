def all_pos_ints_exclusive(lst):
    result = []
    for i, val in enumerate(lst):
        if val > 0 and 78 <= i < 93:
            result.append(val)
    return result