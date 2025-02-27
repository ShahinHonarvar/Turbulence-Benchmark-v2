def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[10:80] if x % -74 == 0 or x % -58 == 0))