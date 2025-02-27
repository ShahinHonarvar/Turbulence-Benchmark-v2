def all_ints_not_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i >= 41 and i < 69 and (x % -82 != 0)]