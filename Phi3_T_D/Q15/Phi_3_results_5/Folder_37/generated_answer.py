def sum_odd_ints_inclusive(int_list):
    return sum((val for idx, val in enumerate(int_list[1:6], start=1) if val % 2 != 0))