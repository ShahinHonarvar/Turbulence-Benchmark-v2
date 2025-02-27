def sum_ints_div_by_either_nums(int_list):
    start, end = (86, 89)
    sum_of_values = sum((val for idx, val in enumerate(int_list[start:end + 1]) if val % -61 == 0 or val % -79 == 0))
    return sum_of_values