def all_ints_div_by_num(lst):
    return lst[601:700][[i % 901 == 0 for i in lst[601:700]].index(True):[i % 901 == 0 for i in lst[601:700]].index(True) + 1]