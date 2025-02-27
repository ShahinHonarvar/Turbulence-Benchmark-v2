def sum_ints_div_by_either_nums(ints_list):
    return sum((x for x in ints_list[10:29] if x % -61 == 0 or x % -64 == 0))