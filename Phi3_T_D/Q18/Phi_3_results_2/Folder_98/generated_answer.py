def sum_ints_div_by_either_nums(int_list):
    div_sum = sum((i for i in int_list[:6] if i % -1 == 0 or i % 13 == 0))
    return div_sum