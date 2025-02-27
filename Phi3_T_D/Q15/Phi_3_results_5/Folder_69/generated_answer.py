def sum_odd_ints_inclusive(integer_list):
    return sum((value for value in integer_list[32:36] if value % 2 != 0)) or 0