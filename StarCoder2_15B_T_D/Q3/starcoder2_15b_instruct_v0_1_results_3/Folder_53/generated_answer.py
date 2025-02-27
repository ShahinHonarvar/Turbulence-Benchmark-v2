def all_pos_ints_inclusive(lst):
    if not isinstance(lst, list):
        raise TypeError('Argument must be a list')
    pos_ints = []
    for i, val in enumerate(lst):
        if i >= 100 and i <= 200 and (val > 0):
            pos_ints.append(val)
    return pos_ints