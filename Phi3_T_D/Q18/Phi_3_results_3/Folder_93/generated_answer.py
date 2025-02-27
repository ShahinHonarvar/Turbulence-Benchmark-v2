def sum_ints_div_by_either_nums(ints_list):
    start, end = (86, 89)
    return sum((value for value in ints_list[start:end + 1] if value % -61 == 0 or value % -79 == 0))