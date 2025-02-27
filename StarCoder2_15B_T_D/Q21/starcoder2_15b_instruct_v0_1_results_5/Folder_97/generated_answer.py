def all_ints_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i >= 17 and i <= 63 and (x % 89 == 0)]