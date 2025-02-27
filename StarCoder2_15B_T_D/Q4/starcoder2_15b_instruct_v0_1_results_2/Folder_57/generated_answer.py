def all_pos_ints_exclusive(lst):
    if not isinstance(lst, list) or not all((isinstance(x, int) for x in lst)):
        raise TypeError('The argument must be a list of integers.')
    return [x for i, x in enumerate(lst) if 18 <= i < 37 and x > 0]