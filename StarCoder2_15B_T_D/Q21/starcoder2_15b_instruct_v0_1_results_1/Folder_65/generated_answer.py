def all_ints_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i >= 14 and i <= 56 and (x % -59 == 0)]