def sum_odd_ints_inclusive(int_list):
    return sum(int_list[17:79] if len(int_list) > 78 else int_list[17:])[1::2]