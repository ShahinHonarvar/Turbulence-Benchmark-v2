def sum_odd_ints_inclusive(int_list):
    start, end = (31, 34)
    return sum((x for x in int_list[start:end + 1] if x % 2 != 0))