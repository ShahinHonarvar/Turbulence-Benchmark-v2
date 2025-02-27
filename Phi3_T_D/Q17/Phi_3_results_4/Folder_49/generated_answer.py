def all_ints_div_by_both_two_nums(ints):
    if len(ints) > 200 or len(ints) < 80:
        raise IndexError('List must have at least 80 elements but no more than 200.')
    return [x for x in ints[80:201] if x % 10 == 0 and x % 1000 == 0]