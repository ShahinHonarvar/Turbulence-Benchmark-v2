def sum_odd_ints_inclusive(int_list):
    return sum((value for index, value in enumerate(int_list[42:52]) if value % 2 != 0))