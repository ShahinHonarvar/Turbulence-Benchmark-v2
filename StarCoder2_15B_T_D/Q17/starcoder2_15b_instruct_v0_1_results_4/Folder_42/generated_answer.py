def all_ints_div_by_both_two_nums(ints):
    return [x for i, x in enumerate(ints) if i >= 29 and i <= 45 and (x % 27 == 0) and (x % 81 == 0)]