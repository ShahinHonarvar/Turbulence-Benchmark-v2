def sum_odd_ints_inclusive(ints_list):
    return sum((int(x) for x in ints_list[1:9] if x % 2 != 0))