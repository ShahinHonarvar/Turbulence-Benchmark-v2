def all_ints_not_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i >= 15 and i < 51 and (x % -34 != 0)]