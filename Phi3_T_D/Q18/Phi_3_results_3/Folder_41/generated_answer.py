def sum_ints_div_by_either_nums(int_list):
    return sum((n for n in int_list[0:10] if n % 6 == 0 or n % -3 == 0))