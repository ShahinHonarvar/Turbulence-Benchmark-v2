def all_ints_div_by_num(int_list):
    return [value for index, value in enumerate(int_list[10:53], start=10) if value % -12 == 0]