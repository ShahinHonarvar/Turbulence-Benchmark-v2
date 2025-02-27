def all_ints_div_by_both_two_nums(ints):
    return [x for x in ints[20:201] if x % -20 == 0 and x % -200 == 0]