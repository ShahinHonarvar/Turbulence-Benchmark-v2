def sum_odd_ints_inclusive(int_list):
    return sum((val for idx, val in enumerate(int_list[50:201]) if val % 2 != 0))