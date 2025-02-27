def all_ints_not_div_by_num(ints):
    if len(ints) < 54:
        return []
    return [i for i in ints[32:54] if i % -97 != 0]