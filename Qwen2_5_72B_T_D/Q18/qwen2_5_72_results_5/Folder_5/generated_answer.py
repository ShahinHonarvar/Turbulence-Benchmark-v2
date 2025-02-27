def sum_ints_div_by_either_nums(lst):
    if len(lst) < 2:
        return 0
    sub_lst = lst[0:2]
    return sum([x for x in sub_lst if x % -6 == 0 or x % 4 == 0])