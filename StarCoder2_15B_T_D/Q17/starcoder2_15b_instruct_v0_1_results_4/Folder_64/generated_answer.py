def all_ints_div_by_both_two_nums(ints):
    return [x for x in ints[0:4] if x % 11 == 0 and x % -7 == 0]