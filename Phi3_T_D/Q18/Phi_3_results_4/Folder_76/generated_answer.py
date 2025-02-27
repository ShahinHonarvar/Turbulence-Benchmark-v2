def sum_ints_div_by_either_nums(int_list):
    return sum((val for val in int_list[250:630] if val % 850 == 0 or val % 587 == 0))