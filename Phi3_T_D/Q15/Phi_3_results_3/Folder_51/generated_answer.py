def sum_odd_ints_inclusive(ints_list):
    return sum((i for i in ints_list[1:9] if i % 2 != 0))