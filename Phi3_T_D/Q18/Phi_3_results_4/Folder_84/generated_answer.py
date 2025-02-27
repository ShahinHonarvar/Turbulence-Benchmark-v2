def sum_ints_div_by_either_nums(int_list):
    return sum((val for val in int_list[78:82] if val % 76 == 0 or val % 60 == 0))