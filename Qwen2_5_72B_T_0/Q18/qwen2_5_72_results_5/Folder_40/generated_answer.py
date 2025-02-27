def sum_ints_div_by_either_nums(lst):
    if len(lst) < 2:
        return 0
    sub_list = lst[0:2]
    return sum([x for x in sub_list if x % 2 == 0 or x % 1 == 0])