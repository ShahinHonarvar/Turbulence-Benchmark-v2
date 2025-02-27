def all_pos_ints_inclusive(arg):
    if not isinstance(arg, list):
        raise TypeError('Argument must be a list')
    new_list = [x for x in arg if x > 0]
    if not all((isinstance(x, int) for x in new_list)):
        raise ValueError('All elements in the list must be positive integers')
    return new_list[55:99]