def sum_ints_div_by_either_nums(int_list):
    sum_val = sum((x for x in int_list[36:86] if x % -27 == 0 or x % -96 == 0))
    return sum_val