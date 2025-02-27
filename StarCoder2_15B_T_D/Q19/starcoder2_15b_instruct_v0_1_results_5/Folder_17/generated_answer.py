def all_ints_not_div_by_num(ints, num=84):
    return [x for i, x in enumerate(ints) if i >= 39 and i < 57 and (x % num != 0)]