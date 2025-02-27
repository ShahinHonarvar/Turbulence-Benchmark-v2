def all_ints_div_by_both_two_nums(ints):
    start, end = (2, 8)
    return [x for x in ints[start:end] if x % -1 == 0 and x % -7 == 0]