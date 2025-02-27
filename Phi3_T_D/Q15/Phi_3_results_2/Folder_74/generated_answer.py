def sum_odd_ints_inclusive(int_list):
    start_index = 17
    end_index = 78
    return sum((x for x in int_list[start_index:end_index + 1] if x % 2 != 0))