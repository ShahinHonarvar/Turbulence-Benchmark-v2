def all_ints_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i >= 40 and i <= 400 and (x % 7 == 0)]