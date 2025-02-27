def sum_ints_div_by_either_nums(int_list):
    return sum((val for val in int_list[28:97] if val % 90 == 0 or val % 97 == 0))