def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[20:201] if x % -20 == 0 or x % -200 == 0))