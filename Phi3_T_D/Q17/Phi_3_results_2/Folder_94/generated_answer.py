def all_ints_div_by_both_two_nums(integers):
    if len(integers) < 95:
        raise ValueError('List must contain at least 95 elements')
    return [value for value in integers[93:95] if value % -53 == 0 and value % -91 == 0]