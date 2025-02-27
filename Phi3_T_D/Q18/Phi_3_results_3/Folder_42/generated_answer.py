def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[29:46] if x % 27 == 0 or x % 81 == 0))