def all_ints_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i >= 1 and i <= 8 and (x % 6 == 0)]