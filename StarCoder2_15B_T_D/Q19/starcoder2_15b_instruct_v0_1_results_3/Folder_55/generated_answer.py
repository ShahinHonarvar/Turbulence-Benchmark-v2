def all_ints_not_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i >= 0 and i < 10 and (x % 10 != 0)]