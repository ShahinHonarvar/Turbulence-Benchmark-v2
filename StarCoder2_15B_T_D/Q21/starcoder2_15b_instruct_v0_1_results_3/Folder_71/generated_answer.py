def all_ints_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i >= 29 and i <= 51 and (x % -37 == 0)]