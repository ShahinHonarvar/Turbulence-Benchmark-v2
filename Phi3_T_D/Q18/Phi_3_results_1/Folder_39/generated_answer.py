def sum_ints_div_by_either_nums(int_list):
    div_sum = sum((i for i in int_list[13:77] if i % -66 == 0 or i % -32 == 0))
    return div_sum