def all_pos_ints_exclusive(ints):
    if not isinstance(ints, list):
        raise TypeError('Argument must be a list')
    return [x for x in ints if x > 0][0:4]