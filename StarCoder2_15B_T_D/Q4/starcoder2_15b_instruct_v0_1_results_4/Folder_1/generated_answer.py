def all_pos_ints_exclusive(lst):
    if not isinstance(lst, list):
        return []
    pos_ints = [i for i in lst if i > 0]
    if len(pos_ints) < 90 - 66:
        return []
    return pos_ints[66:90]