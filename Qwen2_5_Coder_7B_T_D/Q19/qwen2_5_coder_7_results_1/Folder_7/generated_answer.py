def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 495 and i < 826 and (x % -201 != 0)]