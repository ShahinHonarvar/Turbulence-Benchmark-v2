def all_pos_ints_inclusive(lst):
    result = []
    for i, x in enumerate(lst):
        if x > 0 and 34 <= i <= 55:
            result.append(x)
    return result