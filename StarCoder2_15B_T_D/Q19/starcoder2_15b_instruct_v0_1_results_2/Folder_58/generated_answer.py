def all_ints_not_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i >= 266 and i < 586 and (x % 840 != 0)]