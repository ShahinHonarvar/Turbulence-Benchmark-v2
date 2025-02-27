def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 77:
        return 0
    return sum((x for x in int_list[37:77] if x % 2 != 0))