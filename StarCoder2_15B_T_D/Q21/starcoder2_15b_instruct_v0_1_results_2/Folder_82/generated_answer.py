def all_ints_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i >= 0 and i <= 2 and (x % 3 == 0)]