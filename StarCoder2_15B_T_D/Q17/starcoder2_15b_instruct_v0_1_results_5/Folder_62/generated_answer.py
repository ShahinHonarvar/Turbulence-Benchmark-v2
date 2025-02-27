def all_ints_div_by_both_two_nums(ints):
    return [x for i, x in enumerate(ints) if i >= 44 and i <= 59 and (x % 39 == 0) and (x % 15 == 0)]