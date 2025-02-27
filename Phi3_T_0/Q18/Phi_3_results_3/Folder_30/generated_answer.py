def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[10:76 + 1] if x % -81 == 0 or x % -94 == 0))