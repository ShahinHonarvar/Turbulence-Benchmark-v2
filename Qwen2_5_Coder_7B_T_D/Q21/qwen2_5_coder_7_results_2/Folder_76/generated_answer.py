def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 601 and i <= 698 and (x % 901 == 0)]