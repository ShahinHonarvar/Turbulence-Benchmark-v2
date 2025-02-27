def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[25:81] if x % -20 == 0 or x % -26 == 0))