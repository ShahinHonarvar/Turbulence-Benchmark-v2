def sum_odd_ints_inclusive(integer_list):
    return sum((i for i in integer_list[4:9] if i % 2 != 0))