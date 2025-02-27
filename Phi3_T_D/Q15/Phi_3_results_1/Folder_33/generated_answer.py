def sum_odd_ints_inclusive(int_list):
    start, end = (667, 774)
    return sum((i for i in int_list[start:end + 1] if i % 2 == 1))