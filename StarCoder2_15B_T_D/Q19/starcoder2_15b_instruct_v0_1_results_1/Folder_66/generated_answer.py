def all_ints_not_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i in range(84, 86) and x % 99 != 0]