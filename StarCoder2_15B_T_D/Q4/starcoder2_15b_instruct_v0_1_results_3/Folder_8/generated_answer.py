def all_pos_ints_exclusive(lst):
    result = []
    for i, val in enumerate(lst):
        if val > 0 and 56 < i < 92:
            result.append(val)
    return result