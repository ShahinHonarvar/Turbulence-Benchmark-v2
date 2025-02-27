def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[0:8] if x % -9 == 0 or x % -3 == 0))