def sum_ints_div_by_either_nums(int_list):
    result = sum((1 for i in int_list[22:24] if i % -85 == 0 or i % -30 == 0))
    return result