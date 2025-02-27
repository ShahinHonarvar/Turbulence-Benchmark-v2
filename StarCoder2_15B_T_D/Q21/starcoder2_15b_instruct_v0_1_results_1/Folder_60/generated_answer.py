def all_ints_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i >= 31 and i <= 67 and (x % -15 == 0)]