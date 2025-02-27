def sum_ints_div_by_either_nums(int_list):
    return sum((val for idx, val in enumerate(int_list[70:201], start=70) if val % 3 == 0 or val % -300 == 0))