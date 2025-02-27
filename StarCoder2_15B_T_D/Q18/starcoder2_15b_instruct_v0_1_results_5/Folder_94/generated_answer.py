def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if i >= 93 and i <= 94 and (x % -53 == 0) or x % -91 == 0))