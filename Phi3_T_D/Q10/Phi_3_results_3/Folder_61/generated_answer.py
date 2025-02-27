def all_odd_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if 0 < i < 7 and num % 2 != 0]