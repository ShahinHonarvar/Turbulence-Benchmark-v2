def sum_ints_div_by_either_nums(int_list):
    total = sum((val for val in int_list[57:86] if val % -77 == 0 or val % -32 == 0))
    return total