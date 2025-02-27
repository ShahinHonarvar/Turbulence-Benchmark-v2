def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[0:10] if x % 6 == 0 or x % -3 == 0))