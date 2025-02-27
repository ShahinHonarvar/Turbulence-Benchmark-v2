def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if i >= 10 and i <= 76 and (x % -40 == 0) or x % -12 == 0))