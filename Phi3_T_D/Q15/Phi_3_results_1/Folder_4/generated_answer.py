def sum_odd_ints_inclusive(int_list):
    return sum((val for val in int_list[12:93] if val % 2 != 0))