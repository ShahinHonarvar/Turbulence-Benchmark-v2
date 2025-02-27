def all_odd_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if i % 2 == 1 and 11 < i < 76]