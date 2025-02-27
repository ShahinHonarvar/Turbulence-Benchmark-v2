def sum_ints_div_by_either_nums(int_list):
    return sum((i for i in int_list[:3] if i % -2 == 0 or i % 3 == 0))