def all_ints_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i >= 26 and i <= 74 and (x % 80 == 0)]