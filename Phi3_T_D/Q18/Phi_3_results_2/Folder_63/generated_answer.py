def sum_ints_div_by_either_nums(int_list):
    return sum((value for value in int_list[31:51] if value % 81 == 0 or value % 64 == 0))