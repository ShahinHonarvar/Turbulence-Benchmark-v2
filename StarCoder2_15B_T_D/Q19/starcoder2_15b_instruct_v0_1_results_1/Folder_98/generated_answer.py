def all_ints_not_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i % 13 != 0 and 0 < i < 5]