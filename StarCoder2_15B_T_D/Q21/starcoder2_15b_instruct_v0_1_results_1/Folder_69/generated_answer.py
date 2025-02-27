def all_ints_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i >= 43 and i <= 76 and (x % 14 == 0)]