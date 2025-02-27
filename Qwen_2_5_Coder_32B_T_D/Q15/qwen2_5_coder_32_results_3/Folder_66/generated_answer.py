def sum_odd_ints_inclusive(int_list):
    return sum((x for x in int_list[50:55] if x % 2 != 0)) if len(int_list) > 54 else 0