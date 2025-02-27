def sum_ints_div_by_either_nums(int_list):
    sum_div = sum((x for x in int_list[:4] if x % 11 == 0 or x % -7 == 0))
    return sum_div