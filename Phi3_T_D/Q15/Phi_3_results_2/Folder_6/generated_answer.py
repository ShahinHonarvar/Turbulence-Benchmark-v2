def sum_odd_ints_inclusive(int_list):
    return sum((value for value in int_list[10:67] if value % 2 != 0))