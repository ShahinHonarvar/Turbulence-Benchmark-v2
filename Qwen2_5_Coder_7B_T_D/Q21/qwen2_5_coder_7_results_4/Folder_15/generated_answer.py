def all_ints_div_by_num(lst):
    return [x for x in lst if x % 3 == 0 and 0 <= lst.index(x) <= 0]