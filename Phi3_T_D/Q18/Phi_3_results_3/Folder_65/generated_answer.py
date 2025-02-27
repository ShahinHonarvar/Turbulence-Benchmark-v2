def sum_ints_div_by_either_nums(int_list):
    sum_div = sum((i for i in int_list[50:93] if i % -94 == 0 or i % -95 == 0))
    return sum_div