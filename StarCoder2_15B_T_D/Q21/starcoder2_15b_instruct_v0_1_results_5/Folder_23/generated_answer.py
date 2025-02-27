def all_ints_div_by_num(ints):
    return [x for i, x in enumerate(ints) if i >= 59 and i <= 97 and (x % -36 == 0)]