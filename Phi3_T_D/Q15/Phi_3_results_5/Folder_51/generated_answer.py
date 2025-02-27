def sum_odd_ints_inclusive(int_list):
    return sum(int_list[1:9:2]) if any((i % 2 == 1 for i in int_list[1:9])) else 0