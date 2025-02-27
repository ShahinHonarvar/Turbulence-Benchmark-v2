def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst[13:64], start=13) if x % 46 == 0]