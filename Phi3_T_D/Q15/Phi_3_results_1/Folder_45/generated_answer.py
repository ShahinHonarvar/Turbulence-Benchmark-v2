def sum_odd_ints_inclusive(int_list):
    return sum((value for i, value in enumerate(int_list[30:201]) if value % 2 != 0))