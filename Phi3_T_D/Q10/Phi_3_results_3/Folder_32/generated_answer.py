def all_odd_ints_exclusive(int_list):
    start_index, end_index = (11, 76)
    return [x for x in int_list[start_index:end_index] if x % 2 != 0]