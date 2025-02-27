def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if not (199 < i < 201 and x % -200 == 0)]