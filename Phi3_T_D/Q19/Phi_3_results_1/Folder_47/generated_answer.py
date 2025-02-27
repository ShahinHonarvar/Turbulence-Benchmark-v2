def all_ints_not_div_by_num(lst):
    return [x for index, x in enumerate(lst[25:76], start=25) if x % -53 != 0]