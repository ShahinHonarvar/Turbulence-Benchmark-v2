def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[:6] if x % -1 == 0 or x % 13 == 0))