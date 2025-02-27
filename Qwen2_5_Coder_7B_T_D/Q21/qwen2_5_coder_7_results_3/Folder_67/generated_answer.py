def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i in range(40, 69) and x % 16 == 0]