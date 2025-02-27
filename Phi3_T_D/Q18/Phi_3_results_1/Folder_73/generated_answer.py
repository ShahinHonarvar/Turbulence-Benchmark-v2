def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 87:
        return 0
    return sum((value for index, value in enumerate(int_list[81:87], start=81) if value % -33 == 0 or value % -62 == 0))