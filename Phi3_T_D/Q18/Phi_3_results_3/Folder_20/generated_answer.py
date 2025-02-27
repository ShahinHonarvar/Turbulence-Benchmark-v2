def sum_ints_div_by_either_nums(int_list):
    return sum((x for idx, x in enumerate(int_list[48:77], start=48) if x % -46 == 0 or x % -82 == 0))