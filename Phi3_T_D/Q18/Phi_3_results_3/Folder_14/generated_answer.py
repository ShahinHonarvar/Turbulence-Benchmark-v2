def sum_ints_div_by_either_nums(lst):
    sub_list = lst[7:10]
    return sum((x for x in sub_list if x % 2 == 0 or x % 3 == 0))