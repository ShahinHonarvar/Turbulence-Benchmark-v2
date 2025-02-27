def sum_ints_div_by_either_nums(lst):
    return sum((value for value in lst[31:51] if value % 81 == 0 or value % 64 == 0))