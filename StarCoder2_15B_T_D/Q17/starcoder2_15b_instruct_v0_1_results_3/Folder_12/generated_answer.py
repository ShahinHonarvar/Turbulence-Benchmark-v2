def all_ints_div_by_both_two_nums(ints):
    return [x for i, x in enumerate(ints) if i >= 35 and i <= 64 and (x % -30 == 0) and (x % -95 == 0)]