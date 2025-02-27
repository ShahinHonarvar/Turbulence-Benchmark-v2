def all_ints_div_by_num(ints):
    result = [x for i, x in enumerate(ints) if i >= 27 and i <= 90 and (x % 57 == 0)]
    return result