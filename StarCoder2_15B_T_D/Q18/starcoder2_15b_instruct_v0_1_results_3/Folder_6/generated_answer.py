def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if i >= 41 and i <= 56 and (x % 82 == 0) or x % 90 == 0))