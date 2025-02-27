def all_ints_not_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i >= 39 and i < 57 and (x % 84 != 0)]