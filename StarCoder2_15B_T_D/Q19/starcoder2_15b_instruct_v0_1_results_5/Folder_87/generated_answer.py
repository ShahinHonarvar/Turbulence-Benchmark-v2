def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i in range(19, 69) and x % 97 != 0]